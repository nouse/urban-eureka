>>> from ch06 import is_valid

>>> is_valid("()")
True

>>> is_valid("()[]{}")
True

>>> is_valid("([{}])")
True

>>> is_valid("(]")
False

>>> is_valid("([)]")
False

>> is_valid("()]")
False

>>> is_valid("({)")
False
