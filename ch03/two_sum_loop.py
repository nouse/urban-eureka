from typing import List


# start snippet wow
def two_sum(nums: List[int], target: int):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
# end snippet wow
