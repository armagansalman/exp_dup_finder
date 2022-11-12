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
from dataclasses import dataclass
import itertools as IT
#
import types_builtin as B
import types_created as C
#
# B.T == A Generic type.
# B.K == A Generic type.
#
@dataclass
class FnData:
#(
    fn: B.Fn
    argdata: B.Any = None
#)


def ref_get_data(ref: B.T \
        , fn_data: FnData) \
        -> B.K:
    """ ( Returns opaque location for one given item. )

    ( * Might throw exception )
    """
# (
    _fn: B.Fn[[B.T, B.Any], B.K] = fn_data.fn
    _args: B.Any = fn_data.argdata
    
    return _fn(ref, _args)
# )


def ref_set_data(ref: B.T \
        , fn_set:B.Fn[[B.T], B.Bool] \
        , *args \
        , **kwargs) \
        -> B.Bool:
    """ ( Sets some data for one given item. )
    ( Returns True if successfully set. Returns False otherwise.)
    
    ( * Might throw exception )
    """
# (
    result = fn_set(ref, *args, **kwargs)
    
    return result
# )


def ref_len(ref: B.T
        , fn_len: B.Fn[[B.T], B.Int]) \
        -> B.Int:
    """ ( Returns opaque len for one given item. )

    ( * Might throw exception )
    """
# (
    return fn_len(ref)
# )


def ref_bytes(ref: B.T \
        , fn_bytes: B.Fn[[B.T], B.Bytes]) \
        -> B.Bytes:
    """ ( Returns a slice (can be all) of the bytes for one given item. )

    ( * Might throw exception )
    """
# (
    return fn_bytes(ref)
# )


def _group_by_key_helper(ref_key_itr: B.Iter[B.Tuple[B.T, B.K]] \
        , fn_sort_key: B.Fn[ [B.Tuple[B.T, B.K]] , B.Union[B.T, B.K]]) \
        -> B.Iter[B.Tuple[B.K, B.Iter[B.T]]]:
    """ Assumes keys are sortable.
    
    Does what itertools.groupby does. For every group,
    its key is present only once. Not like groupby where every element
    has the key also.
    """
#(
    if type(ref_key_itr) != list:
    #(
        data = list(ref_key_itr)
    #)
    data.sort(key = fn_sort_key)
    
    groups = []
    
    for i in range(1, len(data)):
    #(
        prev = data[i-1]
        curr = data[i]
        key_prev = prev[1]
        key_curr = curr[1]
        
        new_grp = []
        while key_prev == key_curr:
        #(
            new_grp.append()
        #)
        
    #)
    
    return None
#)


def ref_group_by_key(refs: B.Iter[B.T] \
        , fn_key_getter: B.Fn[[B.T], B.K]) \
        -> B.Tuple[B.Iter, B.Iter[C.Error]]:
    """ ( Returns 2-tuple X: X[0] is 2-tuple list Y where first element
    of each tuple of Y is a key and second element is an iterable where each element
    returns that key from fn_key_getter)
    ( key values of references must be sortable. )
    """
# (
    # TODO(armagans): Create (key, ref) iter. | sort by key. (Use itertools.groupby) | Create groups from
    # sorted iterable.
    key_refs: B.List[B.Tuple[B.K, B.T]] = []
    errors: B.List[C.Error] = []
    
    for rf in refs:
    #(
        try:
        #(
            key_res = fn_key_getter(rf)
            key_refs.append( (key_res, rf) )
        #)
        except Exception as Err:
        #(
            errors.append(C.Error(rf, Err))
        #)
    #)
    groups = IT.groupby(key_refs, key = lambda x: x[0])
    
    return (groups, errors)
# )


def main(*args, **kwargs):
#(
    lst: B.List[B.List[B.Int]] = [[1,2,3], [4,5]]
    
    def get_list(lst: B.List[B.List[B.T]] \
            , args = None) \
            -> B.List[B.T]:
    #(
        return lst[0]
    #)
    
    fn_data = FnData(get_list)
    
    itm: B.List[B.Int] = ref_get_data(lst, fn_data)
    itm_2: B.List[B.Bytes] = ref_get_data(lst, fn_data)
    
    def get_len(lst: B.List[B.T]) \
            -> B.Int:
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
    
    to_group = [[1,2],[1,2],[1,3],[1,4],[3,4],[5,6],[7,8],["abc"],999]
    #to_group.sort(key = lambda x: x[0], reverse = True)
    
    print(to_group)
    groups, errors = ref_group_by_key(to_group, fn_key_getter = lambda x: x[0])
    
    for k, grp in groups:
    #(
        print(k)
        print(list(grp))
        print("~~~~~~~~~~~~~")
    #)
    
    print(f"{errors = }")
    for x in errors:
    #(
        print(x)
    #)
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
        return a
        #return [1,2,3] # Should return error with mypy.
    #)
    
    z = fn(x,y)
#)

