from typing import List


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    result = []
    i = 0
    while i < len(nums) - 3:
        j = len(nums) - 1
        while j > i:
            remain = target - nums[i] - nums[j]
            # 内部循环
            # start snippet inner
            k, l = i + 1, j - 1
            while k < l:
                if (s := nums[k] + nums[l]) == remain:
                    result.append([nums[i], nums[k], nums[l], nums[j]])
                    k, l = move(k, nums, 1), move(l, nums, -1)
                elif s > remain:
                    l -= 1
                else:
                    k += 1
            j = move(j, nums, -1)
            # end snippet inner
        i = move(i, nums, 1)
    return result


def move(i, nums, step):
    if step == 0:
        return i

    r = i + step
    while 0 <= r < len(nums) and nums[r] == nums[i]:
        r = r + step
    return r
