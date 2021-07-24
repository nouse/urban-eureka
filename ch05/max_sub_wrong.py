from typing import List


# start snippet wow
def max_sub_array(nums: List[int]) -> int:
    # 构造和目标数组一样长度的数组
    r = nums.copy()
    for i in range(1, len(nums)):
        r[i] = max(nums[i], r[i - 1], nums[i] + r[i - 1])
    # 打印maxSub数组，供检查
    print(r)
    return r[len(r) - 1]
# end snippet wow
