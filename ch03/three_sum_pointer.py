from typing import List


# start snippet wow
def three_sum(nums: List[int], target=0) -> List[List[int]]:
    nums.sort()
    result, outer = [], 0
    while outer < len(nums) - 2:
        i, j = outer + 1, len(nums) - 1
        while i < j:
            if (s := nums[outer] + nums[i] + nums[j]) == target:
                result.append([nums[outer], nums[i], nums[j]])
                i, j = skip_dup(i, nums, 1), skip_dup(j, nums, -1)
            elif s > target:
                j -= 1
            else:
                i += 1
        outer = skip_dup(outer, nums, 1)
    return result
# end snippet wow


def skip_dup(start: int, nums: List, step: int):
    if step == 0:
        return start

    r = start + step
    while 0 <= r < len(nums) and nums[r] == nums[start]:
        r = r + step
    return r
