from ch08 import TreeNode


# start snippet wow
def has_path_sum(root: TreeNode, sum: int) -> bool:
    # 把根节点和目标值加入列表
    choices = [(root, sum)]
    while choices:
        # 从列表后面而不是前面取出节点和目标值
        node, target = choices.pop()
        # 如果节点是叶子节点，且值等于目标值，则返回True结束
        if not node.left and not node.right and\
                node.val == target:
            return True
        # 如果该节点有子节点，把子节点填回列表
        # 新的目标值是目标值减去节点值
        if node.right:
            choices.append((node.right, target - node.val))
        if node.left:
            choices.append((node.left, target - node.val))
    return False
    # end snippet wow
