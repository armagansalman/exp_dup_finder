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
## Non-standard imports:
import F_0x0_ as TD
import F_0x1_ as CB
#)

def GET_FILENAME():
#(
	FILENAME = "procedures_abstract"
	return FILENAME
#)


def abf_get_size(target: TD.Any, get_size_fndata: CB.FuncData) \
		-> TD.Int:
	""" Returns size of given target as an int (at least 0).
		* CAN RAISE EXCEPTION!
		
		Target can be any type of data.
		get_size_fndata has the capability to get given target's size. """
#(
	return CB.call_fndata(target, get_size_fndata)
#)


def abf_get_byte_seq(target: TD.Any, get_bytes_fndata: CB.FuncData) \
		-> TD.Bytes:
	""" Returns sequential bytes from given target.
		* CAN RAISE EXCEPTION!
		
		Target can be any type of data.
		get_bytes_fndata has the capability to get given target's bytes. """
#(
	return CB.call_fndata(target, get_bytes_fndata)
#)



