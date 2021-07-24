>>> from ch08 import path_sum_loop_dfs as has_path_sum
>>> from ch08 import TreeNode

>>> has_path_sum(TreeNode.from_array([5, 4, 8, None, 11, 13, 4, 7, 2, None, None, 1]), 22)
True
>>> has_path_sum(TreeNode.from_array([5, 4, 8, None, 11, 13, 4, 7, 3, None, None, 1]), 22)
False

