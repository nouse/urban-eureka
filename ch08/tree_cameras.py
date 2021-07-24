from enum import Enum
from ch08 import TreeNode


class Status(Enum):
    UNCOVERED = 0
    COVERED = 1
    INSTALLED = 2


# start snippet wow
def min_camera_cover(root: TreeNode) -> int:
    amounts = min_camera(root)
    return min(amounts[0]+1, amounts[1], amounts[2])
# end snippet wow


# start snippet sub
# 返回未覆盖、已覆盖和已安装三种状态下的最少摄像头数量
def min_camera(root):
    if not root:
        # 空节点不可能处于“已安装”状态
        return 0, 0, float("inf")
    lc = min_camera(root.left)
    rc = min_camera(root.right)
    return [
        # 子节点都处于已覆盖状态，亲节点可以是未覆盖状态
        lc[1]+rc[1],
        # 如果任何一个子节点安装了摄像头，亲节点都处于已覆盖状态
        min(lc[2]+rc[1], rc[2]+lc[1], rc[2]+lc[2]),
        # 如果任何一个子节点没有被覆盖，亲节点需要安装摄像头
        min(lc[0]+min(rc), rc[0]+min(lc))+1
    ]
# end snippet sub
