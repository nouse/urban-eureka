>>> from ch11 import exist_array as exist

>>> exist(board=[], word="")
False

>>> exist(board=[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word="ABCCED")
True

>>> exist([["a"]], "ab")
False

>>> exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB")
False
