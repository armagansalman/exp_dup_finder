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
# TODO(armagans): Differences between t_Any && Generic[T]
#
import types_builtin as B
import types_specific as S
#
# B.T == A Generic type.
# B.U == A Generic type.
#
def ref_get_data(ref: B.T
        , fn_getter: B.t_Fn[[B.T], B.U]) \
        -> B.U:
    """ ( Returns opaque location for one given item. )

    ( * Might throw exception )
    """
# (
    return fn_getter(ref)
# )


def ref_set_data(ref: B.T \
        , fn_set:B.t_Fn[[B.T], B.t_Bool] \
        , *args \
        , **kwargs) \
        -> B.t_Bool:
    """ ( Sets some data for one given item. )
    ( Returns True if successfully set. Returns False otherwise.)
    
    ( * Might throw exception )
    """
# (
    result = fn_set(ref, *args, **kwargs)
    
    return result
# )


def ref_len(ref: B.T
        , fn_len: B.t_Fn[[B.T], B.t_Int]) \
        -> B.t_Int:
    """ ( Returns opaque len for one given item. )

    ( * Might throw exception )
    """
# (
    return fn_len(ref)
# )


def ref_bytes(ref: B.T \
        , fn_bytes: B.t_Fn[[B.T], B.t_Bytes]) \
        -> B.t_Bytes:
    """ ( Returns a slice (can be all) of the bytes for one given item. )

    ( * Might throw exception )
    """
# (
    return fn_bytes(ref)
# )



def main(*args, **kwargs):
#(
    lst: B.t_Lst[B.t_Lst[B.t_Int]] = [[1,2,3], [4,5]]
    
    def get_list(lst: B.t_Lst[B.t_Lst[B.T]]) \
            -> B.t_Lst[B.T]:
    #(
        return lst[0]
    #)
    
    itm: B.t_Lst[B.t_Int] = ref_get_data(lst, get_list)
    itm_2: B.t_Lst[B.t_Bytes] = ref_get_data(lst, get_list)
    
    def get_len(lst: B.t_Lst[B.T]) \
            -> B.t_Int:
    #(
        return len(lst)
    #)
    
    len_itm = ref_len(itm, get_len)
    
    assert(len_itm == 3)
    
    assert(itm == lst[0])
    
    assert(bytes(lst[0]) == ref_bytes(itm, lambda x: bytes(x)))
    
    data = 5
    set_func = lambda x,val: x.append(val)
    ref_set_data(lst, set_func, data)
    
    assert(lst[-1] == data)
    
    print(f"~[ INFO ]~ Passed some tests. Module name: `{__name__}`.")
    
#)


if __name__ == "__main__":
#(
    main()
#)




def mypy_test():
#(
    x: int = 5
    y: str = "a"
    
    def fn(a: B.T, b: B.T) -> B.T:
    #(
        return a
    #)
    
    z = fn(x,y) # x,y has different types but mypy accepts this call. Should return error.
#)


def mypy_test_2():
#(
    x: int = 5
    y: str = "a"
    
    def fn(a: B.T, b: B.T) -> B.T:
    #(
        return [1,2,3]
    #)
    
    z = fn(x,y)
#)

