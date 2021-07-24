from bisect import bisect_left
from typing import List


# start snippet wow
def two_sum(nums: List[int], target: int):
    for i in range(0, len(nums) - 1):
        remain = target - nums[i]
        j = bisect_left(nums, remain, i)
        if j != len(nums) and nums[j] == remain:
            return [i, j]
    return []
# end snippet wow
