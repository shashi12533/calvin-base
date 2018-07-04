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
from calvin.actor.actor import Actor, manage, condition, stateguard, calvinsys


class ClassicDelay(Actor):
    """
    After first token, pass on token once every 'delay' seconds.
    Input :
        token: anything
    Outputs:
        token: anything
    """

    @manage(['timer', 'delay', 'started'])
    def init(self, delay):
        self.delay = delay
        self.timer = calvinsys.open(self, "sys.timer.repeating")
        self.started = False

    @stateguard(lambda self: not self.started and calvinsys.can_write(self.timer))
    @condition(['token'], ['token'])
    def start_timer(self, token):
        self.started = True
        calvinsys.write(self.timer, self.delay)
        return (token, )

    @stateguard(lambda self: calvinsys.can_read(self.timer))
    @condition(['token'], ['token'])
    def passthrough(self, token):
        calvinsys.read(self.timer)
        return (token, )

    action_priority = (start_timer, passthrough)
    requires = ['sys.timer.repeating']


    test_kwargs = {'delay': 20}
    test_calvinsys = {'sys.timer.repeating': {'read': ["d", "u", "m", "m", "y"],
                                              'write': [20]}}
    test_set = [
        {
            'inports': {'token': ["a", "b", 1]},
            'outports': {'token': ["a", "b", 1]}
        }
    ]
