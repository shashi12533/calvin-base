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
from calvin.actor.actor import Actor, condition, stateguard, manage


class Alternate2(Actor):
    """
    Alternating between two streams of tokens
    Inputs:
      token_1 : first token stream
      token_2 : second token stream
    Outputs:
        token : resulting token stream
    """

    @manage(['token_one'])
    def init(self):
        self.token_one = True

    def is_even(self):
        return self.token_one

    def is_odd(self):
        return not self.is_even()

    @stateguard(is_even)
    @condition(['token_1'], ['token'])
    def port_one(self, input):
        self.token_one = False
        return (input, )

    @stateguard(is_odd)
    @condition(['token_2'], ['token'])
    def port_two(self, input):
        self.token_one = True
        return (input, )

    action_priority = (port_one, port_two)

    test_set = [
        {
            'inports': {'token_1': [1, 2], 'token_2': ['a', 'b']},
            'outports': {'token': [1, 'a', 2, 'b']}
        },
        {
            'inports': {'token_1': [1]},
            'outports': {'token': [1]}
        }
    ]
