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
#)

#(
## Non-standard imports:
import type_definitions as TD
#)

@dataclass
class FuncData:
	""" ! """
#(
	func: TD.Callable
	argdata: TD.Any
#)


@dataclass
class CallData:
	""" ! """
#(
	target: TD.Any
	fn_val: FuncData
#)

"""
def apply_fn(target: TD.T, fn: TD.Callable):
	# !
#(
	return fn(target)
#)
"""

def fn_apply(target: TD.T, fn_val: FuncData):
	""" ! """
#(
	if fn_val.argdata == None:
	#(
		return fn_val.func(target)
	#)
	return fn_val.func(target, fn_val.argdata)
#)


def invoke(cd: CallData):
	""" ! """
#(
	return fn_apply(cd.target, cd.fn_val)
#)


def test_1():
	""" ! """
#(
	data = [1,2,3]
	
	func = lambda x: len(x)
	
	fnv = FuncData(func, argdata=None)
	
	res = fn_apply(data, fnv)
	res2 = invoke(CallData(data, fnv))
	
	print(res)
	print(res2)
#)


def main(params):
	""" ! """
#(
	test_1()
#)


if __name__ == "__main__":
	""" ! """
#(
	args = None
	
	main(args)
#)

