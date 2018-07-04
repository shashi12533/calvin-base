# -*- coding: utf-8 -*-

# Copyright (c) 2015 Ericsson AB
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

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
from calvin.utilities import dynops

req_type = "placement"

def req_op(node, actor_id=None, component=None, replication_id=None):
    """ Returns any nodes that have replicas of actor """
    if replication_id is None:
        #empty
        it = dynops.List()
        it.set_name("replica_nodes_empty")
        it.final()
        return it
    it = node.storage.get_index_iter(['replicas', 'nodes', replication_id])
    it.set_name("replica_nodes")
    return it
