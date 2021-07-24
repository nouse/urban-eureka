from ch08 import TreeNode


# start snippet wow
def has_path_sum(root: TreeNode, sum: int) -> bool:
    # 返回checkPathSum的第一个返回值（必定为True），
    # 没有则返回False
    return next(check_path_sum(root, sum), False)
# end snippet wow


# start snippet gen
def check_path_sum(root, sum):
    # 如果是叶子节点，且节点的值等于目标值，则yield True
    if not root.left and not root.right and sum == root.val:
        yield True
    # 如果左节点不为空，连接左节点的生成器对象
    if root.left:
        yield from check_path_sum(root.left, sum - root.val)
    # 如果右节点不为空，连接右节点的生成器对象
    if root.right:
        yield from check_path_sum(root.right, sum - root.val)
# end snippet gen
