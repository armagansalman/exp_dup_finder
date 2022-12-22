"""
BSD 3-Clause License

Copyright (c) 2022, Armağan Salman
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

#(
## Standard imports:
from dataclasses import dataclass
	#, field, KW_ONLY
#)

#(
## Non-standard imports:
import F_0x0_ as TD
#)

def GET_FILENAME():
#(
	FILENAME = "compute_base"
	return FILENAME
#)


@dataclass
class FuncData:
	""" ! """
#(
	func: TD.Callable
	data: TD.Any = None
#)


@dataclass
class Command:
	""" ! """
#(
	target: TD.Any
	fn_val: FuncData
#)


def call_func(target: TD.T, func: TD.Callable):
	""" CAN RAISE EXCEPTION! """
#(
	return func(target)
#)


def call_fndata(target: TD.T, fn_val: FuncData):
	""" CAN RAISE EXCEPTION! """
#(
	return fn_val.func(target, fn_val.data)
#)


def call_command(cd: Command):
	""" CAN RAISE EXCEPTION! """
#(
	return call_fndata(cd.target, cd.fn_val)
#)


if __name__ == "__main__":
	""" ! """
#(
	raise Exception("Not Runnable Module.")
#)

