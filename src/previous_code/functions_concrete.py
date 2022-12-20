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

import os

import types_builtin as B
import types_specific as S


def local_file_size(path: B.Str) \
        -> B.Size:
    """docstr"""
# (
    return os.path.getsize(path)
# )


def read_local_file_bytes(file_path: B.Str, staroffset: B.Int,
                          end_offset: B.Int) \
        -> B.Bytes:
    """Returns either the requested byte sequence or throws an Exception.

    * Index values are inclusive.
    """
# (
    # TODO(armagan): Read by chunks.
    with open(file_path, "rb") as in_fobj:
        # (
        if staroffset > 0:
            # (
            in_fobj.seek(staroffset)
        # )
        elif staroffset < 0:
            # (
            raise Exception("Negative staroffset was given for file.")
        # )

        return in_fobj.read(end_offset - staroffset + 1)
    # )
# )


def gelocal_dir_files(dirpath: B.Str) \
        -> B.List[B.Str]:
    """Might throw an Exception."""
# (
    rec_files: B.List = []
    # TODO(armaganslmn): ??? Error handling.
    #ap = os.path.abspath(PATH)

    ap = dirpath
    if os.path.isfile(ap):
        # (
        rec_files.append(ap)
        return rec_files
    # )

    elif os.path.isdir(ap):
        # (
        for root, dirs, files in os.walk(ap):
            # (
            for name in files:
                # (
                p = os.path.join(root, name)
                rec_files.append(p)  # os.path.abspath(p)
            # )
        # )
    # )

    else:  # Link or something else. Ignore them.
        # (
        pass
    # )

    return rec_files
# )
