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


def get_path_str(ref: B.Any, imp_gepath) \
        -> B.Str:
    """Return path str of a file of directory.

    * Might throw exception.
    """
# (
    return imp_gepath(ref)
# )


def iter_get_path_str(ref_iter: S.IterOpak, imp_gepath) \
        -> B.Iter[B.Tuple[B.Any, B.Str]]:
    """Returns (ref, ref's path) tuple.

    * Might throw exception.
    """
# (
    return map(lambda ref: (ref, imp_gepath(ref)), ref_iter)
# )


def gedir_filepaths_recursive(ref_dir: B.Any, imp_gedir_files) \
        -> B.Iter[B.Str]:
    """Returns file path strings. Includes files from subdirectories.

    * Might throw exception.
    """
# (
    return imp_gedir_files(ref_dir)
# )


def iter_get_dir_filepaths_recursive(ref_iter: S.IterOpak, imp_gedir_files) \
        -> B.Iter[B.Tuple[B.Any, B.Iter[B.Str]]]:
    """Returns (ref_dir, file path strings) tuples. Includes files from subdirectories.

    * Might throw exception.
    """
# (
    return map(lambda ref: (ref, imp_gedir_files(ref)), ref_iter)
# )


def get_size(ref: B.Any, imp_get_size) \
        -> B.Size:
    """Returns size (non-negative int) of an object.

    * Might throw exception.
    """
# (
    return imp_get_size(ref)
# )


def iter_get_size(ref_iter: S.IterOpak, imp_get_size) \
        -> B.Iter[B.Tuple[B.Any, B.Size]]:
    """Returns (ref, ref's size) tuple. Size is non-negative int.

    * Might throw exception.
    """
# (
    return map(lambda ref: (ref, imp_get_size(ref)), ref_iter)
# )


def get_bytes(ref: B.Any, imp_get_bytes) \
        -> B.Bytes:
    """Returns byte sequence from given ref.

    * Might throw exception.
    """
# (
    return imp_get_bytes(ref)
# )


def iter_get_bytes(ref_iter: S.IterOpak, imp_get_bytes) \
        -> B.Iter[B.Tuple[B.Any, B.Bytes]]:
    """Returns (ref, ref's byte sequence) tuple.

    * Might throw exception.
    """
# (
    return map(lambda ref: (ref, imp_get_bytes(ref)), ref_iter)
# )
