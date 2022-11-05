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
#(
#)
from pathlib import Path
#
import types_builtin as B
#
def discard_subdirs(refs: B.t_Itr[B.T] \
        , fn_path_getter: B.t_Fn[[B.T], B.t_Str]) \
        -> B.t_Itr[B.T]:
    """ ( Given directories DS, returns a new iterable of directories DR
    where no element of DR is a subdirectory of any element of DS. )
    ( Assumes given paths from refs are valid directories. )
    
    ( * Might throw exception. )
    """
#(
    ref_list: B.t_Lst[B.T] = list(refs)
    
    if len(ref_list) < 2:
        # No subdirs can exist in ref_list. Returns as it is.
    #(
        return ref_list
    #)
    
    ref_path_itr = map(lambda ref: ( ref, Path(fn_path_getter(ref)) ) , ref_list)
    
    # Use absolute paths for later subdir check:
    ref_path_tpls = list(map(lambda tpl: (tpl[0], str(tpl[1].absolute())) , ref_path_itr))
    
    ref_path_tpls.sort(key = lambda x: x[1]) # Key is directory path str.
    
    prev = ref_path_tpls[0]
    
    prev_ref: B.T = prev[0]
    prev_path: B.t_Str = prev[1]
    
    nonsub_dirs = [prev_ref]
    
    for ix in range(1, len(ref_path_tpls)):
        # First one was taken as prev. Start from the second.
    #(
        curr = ref_path_tpls[ix]
        curr_ref: B.T = curr[0]
        curr_path: B.t_Str = curr[1]
        
        prev_ref = prev[0]
        prev_path = prev[1]
        
        if curr_path.startswith(prev_path):
            # Curr_p is a subdir, ignore:
        #(
            pass
        #)
        else:
            # Include curr_ref. İt is not a subdir.
        #(
            nonsub_dirs.append(curr_ref)
        #)
        prev = curr
    #)
    
    return nonsub_dirs
#)


def main(*args, **kwargs):
#(
    DIRS = [ \
        "/home/genel/Documents/Apps/" \
        , "/home/genel/Documents/"
        , "/home/genel" \
        , "/home/genel" \
        , "/home/genel/Downloads/Git_aosa_files/" \
        , "/home/genel/Downloads/" \
        , "/home/genel/Downloadsasd/" \
        ]
    #
    nonsub_dirs = discard_subdirs(DIRS, lambda x: x)
    
    for x in nonsub_dirs:
    #(
        print(x)
    #)
    
#)


if __name__ == "__main__":
#(
    main()
#)
