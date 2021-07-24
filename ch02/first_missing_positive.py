from typing import List


# start snippet wow
def first_missing_positive(nums: List[int]) -> int:
    l = len(nums)
    x = [False] * (l + 1)
    # 遍历给定数组，在新构造的数组中相同的下标填入True
    for i in nums:
        if 0 < i <= l:
            x[i] = True
    # 检查新构造的数组，返回第一个值为False的下标
    for i in range(1, l + 1):
        if not x[i]:
            return i
    # 如果遍历正常结束，返回数组的长度加1
    return l + 1
# end snippet wow
