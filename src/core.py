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

import types_builtin as B
import types_specific as S
import functions_concrete as FConc
import functions_abstract as FAbs


def main(args):
    """docstr"""
# (
    import functools as FT

    data = ["/home/genel/Documents/GiLocal/experimental_dup_finder/src/util.py", "/home/genel/Documents/GiLocal/experimental_dup_finder/src/core.py"
            ]

    """
    sz_iter = FAbs.iter_gesize(data, FConc.local_file_size)
    
    for sz in sz_iter:
        print(sz)
    #
    
    byte_fun = FT.partial(FConc.read_local_file_bytes, staroffset=0, end_offset=16)
    
    bytes_iter = FAbs.iter_gebytes(data, byte_fun)
    
    for x in bytes_iter:
        print(x)
    #
    
    fpaths = FAbs.gedir_filepaths_recursive("/home/genel/Documents/" \
                                            , FConc.gelocal_dir_files)
    #
    for x in fpaths:
        print(x)
    #
    """

    dirs = ["/home/genel/dwhelper/", "/home/genel/Videos/"]
    #

    dir_fpaths_pairs = FAbs.iter_gedir_filepaths_recursive(
        dirs, FConc.gelocal_dir_files)
    #
    for x in dir_fpaths_pairs:
        print(x)
    #
# )


if __name__ == "__main__":
    """docstr"""
# (
    params: B.Dict = dict()

    main(params)
# )
