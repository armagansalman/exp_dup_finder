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
import type_definitions as TD
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
	""" ! """
#(
	return func(target)
#)


def call_fndata(target: TD.T, fn_val: FuncData):
	""" ! """
#(
	return fn_val.func(target, fn_val.data)
#)


def call_command(cd: Command):
	""" ! """
#(
	return call_fndata(cd.target, cd.fn_val)
#)


def test_1():
	""" ! """
#(
	data = [1,2,3]
	
	func = lambda x, DATA: len(x)
	
	fnv = FuncData(func)
	
	res = call_fndata(data, fnv)
	res2 = call_command(Command(data, fnv))
	
	assert(res == res2)
	# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	return True
#)


def test_2():
	""" ! """
#(
	data = [1,2,3]
	
	def fn_adder(t, DATA):
	#(
		return t + DATA[0]
	#)
	
	fndata_10_adder = FuncData(fn_adder, (10,)) # arg given using Tuple
	
	res = call_fndata(data[0], fndata_10_adder)
	assert(res == data[0] + 10)
	# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	fndata_10_adder2 = FuncData(fn_adder, [10]) # arg given using List
	
	res2 = call_fndata(data[-1], fndata_10_adder)
	assert(res2 == data[-1] + 10)
	
	return True
#)


def test_3():
	""" ! """
#(
	data = [1,2,3]
	
	def fn_mult(t, DATA):
	#(
		return t * DATA["multiplier"]
	#)
	
	fndata_10_mult = FuncData(fn_mult, {"multiplier": 10}) # arg given using Tuple
	
	res = call_fndata(data[0], fndata_10_mult)
	assert(res == data[0] * 10)
	# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	
	return True
#)


def main(params):
	""" ! """
#(
	tests = [ \
		(test_1, "Test | call_fndata, call_command ; None argument") \
		,(test_2, "Test | with argument; sequence type argument") \
		,(test_3, "Test | with argument; dictionary type argument") \
			]
	#
	
	for fn_test, summary in tests:
	#(
		print(f"<[ INFO ]> Running: {fn_test.__name__}")
		print(f"Summary: {summary}")
		
		fn_test()
	#)
	
	print("<[ INFO ]> All tests PASSED.")
#)


if __name__ == "__main__":
	""" ! """
#(
	args = None
	
	main(args)
#)

