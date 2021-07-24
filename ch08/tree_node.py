from typing import Type, List
from collections import deque


class TreeNode:
    __slots__ = "val", "left", "right"

    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.to_array())

    def to_array(self) -> List[int]:
        choices = deque([self])
        o = []
        while any(choices):
            c = choices.popleft()
            if not c:
                o.append(None)
                continue
            o.append(c.val)
            if c.left or c.right or choices:
                choices.append(c.left)
            if c.right or choices:
                choices.append(c.right)

        return o

    @staticmethod
    def from_array(arr: List[int]):
        if not arr:
            return None
        r = TreeNode(arr[0])
        t = r
        list = deque([])

        for i in range(1, len(arr)):
            v = None
            if arr[i]:
                v = TreeNode(arr[i])
                list.append(v)
            if i % 2 == 1:
                t.left = v
            else:
                t.right = v
                t = list.popleft()

        return r
