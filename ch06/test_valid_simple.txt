>>> from ch06 import is_valid_simple as is_valid

>>> is_valid("()(())")
True

>>> is_valid("()())")
False

>>> is_valid("(()(())")
False
