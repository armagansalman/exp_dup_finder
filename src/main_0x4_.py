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
# import os
#)

#(
## Non-standard imports:
import type_definitions_0x0_ as TD
import compute_base_0x1_ as CB
import procedures_abstract_0x2_ as PrcAbs
import procedures_concrete_0x3_ as PrcCon
#)

def GET_FILENAME():
#(
	FILENAME = "main"
	return FILENAME
#)


def test_get_size():
	""" a """
#(
	fname = "./example_file_0x7_.txt" # 10 byte file.
	FSIZE = 10
	
	fdat = CB.FuncData(PrcCon.get_size_local_file)
	
	fsz = PrcAbs.abf_get_size(fname, fdat)
	
	assert(fsz == FSIZE)
#)


def test_get_bytes():
	""" a """
#(
	fname = "./example_file_0x7_.txt" # 10 byte file.
	byte_seq: bytes = bytes("123", encoding="utf-8")
	
	fdata = {"start_index":0, "end_index": 2} # First 3 bytes.
	fdat = CB.FuncData(PrcCon.get_bytes_local_file, fdata)
	
	fbytes: bytes = PrcAbs.abf_get_byte_seq(fname, fdat)
	
	assert(fbytes == byte_seq)
#)


def test_hash():
	""" ! """
#(
	import hash_0x8_ as HASH
	
	S = bytes("abcdef", encoding="utf-8")
	
	dgst = HASH.sha512_bytes_digest(S)
	
	print(f"Bytes digest byte count: {len(dgst)}")
	
#)

def main(params):
	""" ! """
#(
	tests = [ \
		(test_get_size, "Test | local file size retrieve test") \
		,(test_get_bytes, "Test | local file bytes retrieve test") \
		,(test_hash, "Test | hash functions") \
		]
	#
	
	print(f"<[ INFO ]> Running FILENAME: {GET_FILENAME()}")
	
	for fn_test, summary in tests:
	#(
		print(f"<[ INFO ]> Running Function: {fn_test.__name__}")
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
