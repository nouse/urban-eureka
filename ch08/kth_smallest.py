from typing import Generator

from ch08 import TreeNode


# start snippet wow
def kth_smallest(root: TreeNode, k: int) -> int:
    # 不断地从遍历函数接收返回值，同时减小计数器
    for i in inorder(root):
        # 计数器为0，说明是第k小的值，返回该值
        if (k := k-1) == 0:
            return i
# end snippet wow


# start snippet inorder
def inorder(root: TreeNode) -> Generator[int, None, None]:
    if root:
        # 参考二叉搜索树的定义，
        # 按照 左子树-根节点-右子树 的顺序遍历
        yield from inorder(root.left)
        yield root.val
        yield from inorder(root.right)
# end snippet inorder
