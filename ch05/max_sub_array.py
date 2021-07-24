from typing import List


# start snippet wow
def max_sub_array(nums: List[int]) -> int:
    # 构造和目标数组一样长度的数组
    r = nums.copy()
    for i in range(1, len(nums)):
        # 如果max_sub[i-1]大于零，则填入max_sub[i-1]，
        # 否则为nums[i]
        if r[i - 1] > 0:
            r[i] += r[i - 1]
    # 打印maxSub数组，供检查
    print(r)
    return max(r)
# end snippet wow
