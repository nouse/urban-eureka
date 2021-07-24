import sys
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    i = 0
    while i < len(nums) - 2:
        target = -nums[i]
        # start snippet inner
        h = {}
        j = i + 1
        while j < len(nums):
            if (c := nums[j]) in h:
                result.append([
                    nums[i],
                    h[c],
                    nums[j]])
                j = skip_dup(j, nums)
            else:
                h[target - c] = c
                j += 1

        i = skip_dup(i, nums)
        # end snippet inner
    return result


# start snippet skip_dup
def skip_dup(start: int, nums: List[int]) -> int:
    n = start + 1
    while n < len(nums) and nums[n] == nums[start]:
        n += 1
    return n
# end snippet skip_dup
