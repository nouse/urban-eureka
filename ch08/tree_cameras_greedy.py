from enum import Enum

from ch08 import TreeNode


# start snippet wow
def min_camera_cover(root: TreeNode) -> int:
    amount, s = min_camera(root)
    # 如果根节点处于未覆盖状态，加1再返回
    if s == Status.UNCOVERED:
        return amount+1
    return amount
# end snippet wow


class Status(Enum):
    UNCOVERED = 0
    COVERED = 1
    INSTALLED = 2


# start snippet sub
def min_camera(root):
    if not root:
        # 空节点属于“已覆盖”状态，不需要亲节点安装摄像头
        return 0, Status.COVERED
    lc, ls = min_camera(root.left)
    rc, rs = min_camera(root.right)
    # 如果任何一个子节点没有被覆盖，亲节点需要安装摄像头
    if ls == Status.UNCOVERED or rs == Status.UNCOVERED:
        return lc+rc+1, Status.INSTALLED
    # 如果任何一个子节点安装了摄像头，亲节点处于已覆盖状态
    if ls == Status.INSTALLED or rs == Status.INSTALLED:
        return lc+rc, Status.COVERED
    return lc+rc, Status.UNCOVERED
# end snippet sub
