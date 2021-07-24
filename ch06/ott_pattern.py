from typing import List


def find132pattern(nums: List[int]) -> bool:
    if not nums:
        return False
    # start snippet wow
    stack = [nums[-1]]
    floor = float("-inf")
    for i in range(len(nums) - 1, 0, -1):
        n = nums[i - 1]
        # floor初始值为负无穷, 保证没有找到k和j时，此处为False
        if n < floor:
            return True

        while len(stack) > 0 and n > stack[-1]:
            floor = stack.pop()

        stack.append(n)

    return False
    # end snippet wow
