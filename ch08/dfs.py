from ch08 import TreeNode


# start snippet wow
def dfs(root: TreeNode):
    # 遍历顺序：val -> left -> right
    yield root.val
    if root.left:
        yield from dfs(root.left)
    if root.right:
        yield from dfs(root.right)
# end snippet wow
