from typing import List
# correct
ib:int = 1
# wrong
ia:int = 1.3
# correct
is_trueb: bool = True
# wrong
is_truec: bool = 1
is_truea: bool = 1.2
# correct
a:List = []
# wrong
aa:List = {}
"""
wrong_type.py:5: error: Incompatible types in assignment (expression has type "float", variable has type "int")
wrong_type.py:7: error: Incompatible types in assignment (expression has type "int", variable has type "bool")
wrong_type.py:10: error: Incompatible types in assignment (expression has type "float", variable has type "bool")
wrong_type.py:14: error: Incompatible types in assignment (expression has type "Dict[<nothing>, <nothing>]", variable has type "List[Any]")
Found 4 errors in 1 file (checked 1 source file)

"""

