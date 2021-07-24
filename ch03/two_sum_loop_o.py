from typing import List


# start snippet wow
def two_sum(nums: List[int], target: int):
    for i in range(len(nums)-1):
        remain = target - nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] == remain:
                return [i, j]
    return []
# end snippet wow
