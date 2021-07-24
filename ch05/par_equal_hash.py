from typing import List


def can_partition(nums: List[int]) -> bool:
    nums.sort()
    if len(nums) < 2:
        return False
    s = sum(nums)
    if s % 2 == 1:
        return False
    target = s // 2

    # start snippet wow
    # 构造哈希表，初始值为空
    d = {}
    for n in nums:
        # 相同逻辑，如果遍历的元素已经比目标值大，搜索结束
        if n > target:
            break
        # 遍历现有的键，填入新的键值对
        for k in list(d):
            if k + n <= target:
                d[k + n] = True
        d[n] = True
        # 判断target是否已填入True，是则函数结束，返回True
        if target in d:
            return True
    return False
    # end snippet wow
