# -*- coding: utf-8 -*-

# Copyright (c) 2017 Ericsson AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy
import json
from twisted.enterprise import adbapi
from twisted.internet import defer
from calvin.runtime.south.plugins.async import async
from calvin.runtime.north.plugins.storage.storage_base import StorageBase
from calvin.utilities.calvin_callback import CalvinCB
from calvin.utilities import calvinlogger
from calvin.utilities import calvinconfig

_log = calvinlogger.get_logger(__name__)
_conf = calvinconfig.get()

############################
# TODO Remake the storage API:
# * better names needed
# * append and remove should provid a list of serialized values not a serialized list
# * delete should be exposed properly, not only set with None
# * index should be exposed directly by storage plugin to allow engine optimizations
######################

# The config kwarg depends on which database python module that is used
# Here is data for dbmodule="MySQLdb"
# host, port, db, user and passwd can be set, but if local only user and passwd is needed
# If other modules use another arg name for db need to fix that here
# Below defaults assume a password-less root user on local mysql
config_kwargs = _conf.get('global', 'storage_sql')
config_kwargs.setdefault('dbmodule', "MySQLdb")
config_kwargs.setdefault('user', "root")
config_kwargs.setdefault('db', _conf.get_in_order("dht_network_filter", "ALL").replace("-", "_"))

# Have single values and set-values in seperate tables to allow uniqueness on the right terms, 
# i.e. key and key+value, respectively. Also support longer valuestr in single value.
# Set-values have one value on each row in the table.
QUERY_SETUP = """
CREATE DATABASE {db};
CREATE TABLE {db}.ckeys (
    id BIGINT AUTO_INCREMENT,
    keystr VARCHAR(1024),
    PRIMARY KEY(id),
    INDEX(keystr),
    UNIQUE(keystr)
);
CREATE TABLE {db}.cvalues (
    id BIGINT NOT NULL,
    valuestr VARCHAR(2048),
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES {db}.ckeys (id) ON DELETE CASCADE
);
CREATE TABLE {db}.csetvalues (
    id BIGINT NOT NULL,
    valuestr VARCHAR(512),
    UNIQUE KEY keyvalue (id, valuestr),
    FOREIGN KEY (id) REFERENCES {db}.ckeys (id) ON DELETE CASCADE
);""".format(db=config_kwargs['db'])

# Needed to make set two roundtrips since mysql did not like (Err 2014) multi-statement that modified a depedent table
# Could potentially be made if multi-statement is supported in the dbmodule (now using MySQLdb module)
QUERY_SET = [q.format(db=config_kwargs['db']) for q in ["""
INSERT IGNORE INTO {db}.ckeys (keystr) VALUES('{{keystr}}');
""", """
INSERT INTO {db}.cvalues (id, valuestr)
    (SELECT id, '{{valuestr}}' FROM {db}.ckeys WHERE keystr='{{keystr}}')
    ON DUPLICATE KEY UPDATE valuestr='{{valuestr}}';
"""]]

QUERY_GET = """
SELECT valuestr FROM {db}.cvalues WHERE id IN (SELECT id FROM {db}.ckeys WHERE keystr='{{keystr}}');
""".format(db=config_kwargs['db'])

# Due to value tabels have foreign key for id the values will also be deleted
QUERY_DELETE = """
DELETE FROM {db}.ckeys WHERE keystr='{{keystr}}';
""".format(db=config_kwargs['db'])

QUERY_APPEND = [q.format(db=config_kwargs['db']) for q in ["""
INSERT IGNORE INTO {db}.ckeys (keystr) VALUES('{{keystr}}');
""", """
INSERT IGNORE INTO {db}.csetvalues (id, valuestr)
    (SELECT id, '{{valuestr}}' FROM {db}.ckeys WHERE keystr='{{keystr}}');
"""]]

QUERY_REMOVE = """
DELETE FROM {db}.csetvalues WHERE
    id IN (SELECT id FROM {db}.ckeys WHERE keystr='{{keystr}}') AND valuestr='{{valuestr}}';
""".format(db=config_kwargs['db'])

QUERY_GETCONCAT = """
SELECT valuestr FROM {db}.csetvalues WHERE
    id IN (SELECT id FROM {db}.ckeys WHERE keystr='{{keystr}}');
""".format(db=config_kwargs['db'])

class SqlClient(StorageBase):
    """
        Sql client plugin class for SQL based storage.
    """
    def __init__(self):
        super(SqlClient, self).__init__()
        self.dbpool = None

    def start(self, iface='', bootstrap=[], cb=None, name=None, nodeid=None):
        kwargs = copy.copy(config_kwargs)
        _log.debug("SQL start %s" % str(kwargs))
        kwargs.pop('db', None)
        dbmodule = kwargs.pop('dbmodule', "MySQLdb")
        # FIXME does this take too long?
        self.dbpool = adbapi.ConnectionPool(dbmodule, **kwargs)
        if not self.dbpool:
            _log.debug("Failed SQL connection pool")
            if cb is not None:
                async.DelayedCall(0, cb, False)
            return
        d = self.dbpool.runQuery(QUERY_SETUP)
        d.addCallbacks(CalvinCB(self._setup_cb, cb=cb), CalvinCB(self._setup_fail_cb, cb=cb))
        _log.debug("Sent SQL table setup query")

    def _setup_cb(self, result, *args, **kwargs):
        cb = kwargs.pop('cb', None)
        _log.debug("SQL setup OK %s" % str(result))
        if cb is not None:
            async.DelayedCall(0, cb, True)

    def _setup_fail_cb(self, failure, **kwargs):
        ok = False
        cb = kwargs.pop('cb', None)
        try:
            err = int(str(failure.value)[1:5])
        except:
            err = 9999
        if err == 1007:
            # Database exist, which is OK
            ok = True
        _log.debug("SQL setup %s %i %s" % ("OK" if ok else "FAIL", err, str(failure)))
        if cb is not None:
            async.DelayedCall(0, cb, ok)

    def set(self, key, value, cb=None):
        """
            Set a key, value pair in the storage
        """
        _log.debug("SQL set %s to %s" % (key, value))
        if value is None:
            # This is actually a delete (an actual None would be serialized)
            _log.debug("SQL delete %s" % (key,))
            d1 = self.dbpool.runQuery(QUERY_DELETE.format(keystr=key, valuestr=value))
            d1.addCallbacks(CalvinCB(self._set_cb, cb=cb, key=key, value=value),
                            CalvinCB(self._set_fail_cb, cb=cb, key=key, value=value))
            return

        def _set_value(*args, **kwargs):
            d2 = self.dbpool.runQuery(QUERY_SET[1].format(keystr=key, valuestr=value))
            d2.addCallbacks(CalvinCB(self._set_cb, cb=cb, key=key, value=value),
                            CalvinCB(self._set_fail_cb, cb=cb, key=key, value=value))
        d1 = self.dbpool.runQuery(QUERY_SET[0].format(keystr=key, valuestr=value))
        d1.addCallbacks(_set_value, CalvinCB(self._set_fail_cb, cb=cb, key=key, value=value))
        _log.debug("SQL set %s to %s requested" % (key, value))

    def _set_cb(self, result, **kwargs):
        _log.debug("SQL set OK")
        cb = kwargs.pop('cb', None)
        key = kwargs.pop('key', None)
        value = kwargs.pop('value', None)
        _log.debug("SQL set OK %s" % str(result))
        if cb is not None:
            async.DelayedCall(0, CalvinCB(cb, key, value))

    def _set_fail_cb(self, failure, **kwargs):
        _log.debug("SQL set FAIL")
        ok = False
        cb = kwargs.pop('cb', None)
        key = kwargs.pop('key', None)
        # TODO handle errors
        try:
            err = int(str(failure.value)[1:5])
        except:
            err = 9999
        _log.debug("SQL set %s %i %s" % ("OK" if ok else "FAIL", err, str(failure)))
        if cb is not None:
            async.DelayedCall(0, CalvinCB(cb, key, value if ok else None))

    def get(self, key, cb=None):
        """
            Gets a value from the storage
        """
        _log.debug("SQL get %s" % (key,))
        d = self.dbpool.runQuery(QUERY_GET.format(keystr=key))
        d.addCallbacks(CalvinCB(self._get_cb, cb=cb, key=key), CalvinCB(self._get_fail_cb, cb=cb, key=key))
        _log.debug("SQL get %s requested" % (key,))

    def _get_cb(self, result, **kwargs):
        _log.debug("SQL get OK")
        cb = kwargs.pop('cb', None)
        key = kwargs.pop('key', None)
        try:
            r = result[0][0]
        except:
            # Empty hence deleted or don't exist (DHT differentiate between these, False and None respectievly)
            # SQL always give None
            r = None
        _log.debug("SQL get OK %s" % r)
        if cb is not None:
            async.DelayedCall(0, CalvinCB(cb, key, r))

    def _get_fail_cb(self, failure, **kwargs):
        _log.debug("SQL get FAIL")
        ok = False
        cb = kwargs.pop('cb', None)
        key = kwargs.pop('key', None)
        # TODO handle errors
        try:
            err = int(str(failure.value)[1:5])
        except:
            err = 9999
        _log.debug("SQL get %s %i %s" % ("OK" if ok else "FAIL", err, str(failure)))
        if cb is not None:
            async.DelayedCall(0, CalvinCB(cb, key, None))

    def get_concat(self, key, cb=None):
        """
            Gets a value from the storage
        """
        _log.debug("SQL get_concat %s" % (key,))
        d = self.dbpool.runQuery(QUERY_GETCONCAT.format(keystr=key))
        d.addCallbacks(CalvinCB(self._getconcat_cb, cb=cb, key=key), CalvinCB(self._getconcat_fail_cb, cb=cb, key=key))
        _log.debug("SQL get_concat %s requested" % (key,))

    def _getconcat_cb(self, result, **kwargs):
        _log.debug("SQL get_concat OK %s" % str(result))
        cb = kwargs.pop('cb', None)
        key = kwargs.pop('key', None)
        r = "[" + ",".join([r[0] for r in result]) + "]"
        _log.debug("SQL get_concat OK %s %s" % (result, r))
        if cb is not None:
            async.DelayedCall(0, CalvinCB(cb, key, r))

    def _getconcat_fail_cb(self, failure, **kwargs):
        _log.debug("SQL get_concat FAIL")
        ok = False
        cb = kwargs.pop('cb', None)
        key = kwargs.pop('key', None)
        # TODO handle errors
        try:
            err = int(str(failure.value)[1:5])
        except:
            err = 9999
        _log.debug("SQL get_concat %s %i %s" % ("OK" if ok else "FAIL", err, str(failure)))
        if cb is not None:
            async.DelayedCall(0, CalvinCB(cb, key, None))

    def append(self, key, value, cb=None):
        _log.debug("SQL append %s to %s" % (value, key))
        # Make serialized list of values into a list of serialized values
        # Assumes JSON coded
        # TODO change the storage API, to provide the list of serialized values
        values = [json.dumps(v) for v in json.loads(value)]
        def _append_value(*args, **kwargs):
            dlist = []
            for v in values:
                dlist.append(self.dbpool.runQuery(QUERY_APPEND[1].format(keystr=key, valuestr=v)))
            d2 = defer.DeferredList(dlist) if len(dlist) > 1 else dlist[0]
            d2.addCallbacks(CalvinCB(self._append_cb, cb=cb, key=key, value=value), CalvinCB(self._append_fail_cb, cb=cb, key=key, value=value))
        d1 = self.dbpool.runQuery(QUERY_APPEND[0].format(keystr=key))
        d1.addCallbacks(_append_value, CalvinCB(self._append_fail_cb, cb=cb, key=key, value=value))
        _log.debug("SQL append %s to %s requested" % (value, key))

    def _append_cb(self, result, **kwargs):
        _log.debug("SQL append OK")
        cb = kwargs.pop('cb', None)
        key = kwargs.pop('key', None)
        value = kwargs.pop('value', None)
        _log.debug("SQL append OK %s" % str(result))
        if cb is not None:
            async.DelayedCall(0, CalvinCB(cb, key, value))

    def _append_fail_cb(self, failure, **kwargs):
        _log.debug("SQL append FAIL")
        ok = False
        cb = kwargs.pop('cb', None)
        key = kwargs.pop('key', None)
        # TODO handle errors
        try:
            err = int(str(failure.value)[1:5])
        except:
            err = 9999
        _log.debug("SQL append %s %i %s" % ("OK" if ok else "FAIL", err, str(failure)))
        if cb is not None:
            async.DelayedCall(0, CalvinCB(cb, key, value if ok else None))

    def remove(self, key, value, cb=None):
        _log.debug("SQL remove %s to %s" % (value, key))
        # Make serialized list of values into a list of serialized values
        # Assumes JSON coded
        # TODO change the storage API, to provide the list of serialized values
        values = [json.dumps(v) for v in json.loads(value)]
        dlist = []
        for v in values:
            dlist.append(self.dbpool.runQuery(QUERY_REMOVE.format(keystr=key, valuestr=v)))
        d = defer.DeferredList(dlist) if len(dlist) > 1 else dlist[0]
        d.addCallbacks(CalvinCB(self._remove_cb, cb=cb, key=key, value=value), CalvinCB(self._remove_fail_cb, cb=cb, key=key, value=value))
        _log.debug("SQL remove %s to %s requested" % (value, key))

    def _remove_cb(self, result, **kwargs):
        _log.debug("SQL remove OK")
        cb = kwargs.pop('cb', None)
        key = kwargs.pop('key', None)
        value = kwargs.pop('value', None)
        _log.debug("SQL remove OK %s" % str(result))
        if cb is not None:
            async.DelayedCall(0, CalvinCB(cb, key, value))

    def _remove_fail_cb(self, failure, **kwargs):
        _log.debug("SQL remove FAIL")
        ok = False
        cb = kwargs.pop('cb', None)
        key = kwargs.pop('key', None)
        # TODO handle errors
        try:
            err = int(str(failure.value)[1:5])
        except:
            err = 9999
        _log.debug("SQL remove %s %i %s" % ("OK" if ok else "FAIL", err, str(failure)))
        if cb is not None:
            async.DelayedCall(0, CalvinCB(cb, key, value if ok else None))

    def bootstrap(self, addrs, cb=None):
        _log.debug("SQL bootstrap")

    def stop(self, cb=None):
        _log.debug("SQL stop")