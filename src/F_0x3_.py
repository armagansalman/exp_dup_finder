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
import os
#)

#(
## Non-standard imports:
import F_0x0_ as TD
import F_0x1_ as CB
#)

def GET_FILENAME():
#(
	FILENAME = "procedures_concrete"
	return FILENAME
#)


def get_size_local_file(file_path: TD.Str, DATA: TD.Any) -> TD.Int:
	""" Returns local file size (in bytes) as an int. At least 0.
		* CAN RAISE EXCEPTION!
		file_path can be any valid path string.
		DATA can be any type of data. Currently not used. """
#(
	return os.path.getsize(file_path)
#)


def get_bytes_local_file(file_path: TD.Str, DATA: TD.Any) -> TD.Bytes:
	""" Returns byte sequence from given local file path.
		* CAN RAISE EXCEPTION!
		Indices are both inclusive. """
#(
	start_index = DATA["start_index"]
	end_index = DATA["end_index"]
	
	with open(file_path, "rb") as in_fobj:
		# (
		if start_index == 0:
			# (
			return in_fobj.read(end_index - start_index + 1)
		# )
		else:
			# (
			in_fobj.seek(start_index)
			return in_fobj.read(end_index - start_index + 1)
		# )
	# )
#)


