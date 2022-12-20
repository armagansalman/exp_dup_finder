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
#
#
import os
#
import types_builtin as B
#(
#)


def gefpaths_recursively(PATH: B.Str) \
        -> B.List[B.Str]:
#(
    rec_files: list = []
    # TODO(armaganslmn): ??? Error handling.
    #ap = os.path.abspath(PATH)
    
    ap = PATH
    if os.path.isfile(ap):
    #(
        rec_files.append(ap)
        return rec_files
    #)
    
    elif os.path.isdir(ap):
    #(
        for root, dirs, files in os.walk(ap):
        #(
            for name in files:
            #(
                p = os.path.join(root, name)
                rec_files.append(p) #os.path.abspath(p)
            #)
        #)
    #)
    
    else: # Link or something else. Ignore them.
    #(
        pass
    #)
    
    return rec_files
#)


def gefpaths_from_path_iter(paths_iter: B.List[B.Str]):
#(
    if type(paths_iter[0]) != B.Str or type(paths_iter[-1]) != B.Str:
    #(
        raise Exception("A list of B.Str must be given.")
    #)
    
    file_paths: list = []
    
    # Below line removed. Selection belongs to mdl_Traverser module.
    # unq_paths = set(map(lambda x: x.path_str , paths_iter))
    
    # TODO(armaganslmn): Handle if input is file.
    # TODO(armaganslmn): ??? Error handling.
    
    #path_strings = map(lambda x: x.path_str , paths_iter)
    path_strings = paths_iter
    
    for string in path_strings:
    #(
        file_paths.extend( gefpaths_recursively(string) )
    #)
    
    return file_paths
#)


def main(*args, **kwargs):
#(
    raise Exception("Not runnable.")
#)


if __name__ == "__main__":
#(
    main()
#)
