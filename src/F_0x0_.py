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

from typing import Iterable as Iter
from typing import List
from typing import Set
from typing import Tuple
from typing import Dict
from typing import Callable
from typing import Any
from typing import Hashable
from typing import Optional as Opt
from typing import ItemsView
from typing import Sequence as Seq
from typing import Union
from typing import TypeVar

def GET_FILENAME():
#(
	FILENAME = "type_definitions"
	return FILENAME
#)

Bool = bool
Int = int
Str = str
Bytes = bytes

IterHashable = Iter[Hashable]

T = TypeVar('T')
K = TypeVar('K')

# Custom type definitions:
NumNatural = Int  # Starts from 0.
Size = NumNatural


class Type_Void:
	""" Is used to check if a reference holds a valid value or not.
	No other object can be this type.
	This type has no instance. Only its type is used.
	If a variable is of this type, IT SHALL NOT BE USED.
	"""
#(
	pass
#)
Void = Type_Void

def is_void(target):
#(
	return target == Void or isinstance(target, Void)
#)


def main(params):
	""" ! """
#(
	assert(is_void([1,2,3,4]) == False)
	
	assert(is_void(Void()) == True)
	
	assert(is_void(Void) == True)
	
	print("<[ INFO ]> All tests PASSED.")
#)


if __name__ == "__main__":
	""" ! """
#(
	args = None
	
	main(args)
#)
