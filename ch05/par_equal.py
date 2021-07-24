from typing import List


# start snippet start
def can_partition(nums: List[int]) -> bool:
    # 排除掉总和为奇数的数组，并构造待填充的数组。
    nums.sort()
    if len(nums) < 2:
        return False
    s = sum(nums)
    if s % 2 == 1:
        return False
    target = s // 2

    a = [False] * (target + 1)
    # end snippet start

    # start snippet wow
    for n in nums:
        # 如果遍历的元素已经比目标值大，说明没有找到结果，搜索结束
        if n > target:
            break
        # 遍历数组，如果该位置已经为True，则偏移n个位置也填上True
        for i in reversed(range(0, target + 1 - n)):
            if a[i]:
                a[i + n] = True
        a[n] = True
        # 判断target是否已填入True，是则函数结束，返回True
        if a[target]:
            return True
    return False
    # end snippet wow
