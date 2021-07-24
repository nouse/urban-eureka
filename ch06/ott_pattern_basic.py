from typing import List


def find132pattern(nums: List[int]) -> bool:
    if not nums:
        return False
    # start snippet split
    stack, ranges = [nums[0]], []
    for i in range(1, len(nums)):
        n = nums[i]

        # 如果n小于栈顶元素，说明打破了连续增长，
        # 把当前栈的最大最小值填入数组。
        if n < stack[-1]:
            if len(stack) > 1:
                ranges.append((stack[0], stack[-1]))
            stack = []

        # 否则进行入栈操作，保证栈是从大到小
        stack.append(n)
    # end snippet split

        if in_ranges(n, ranges):
            return True

    return False


# start snippet match
def in_ranges(n: int, ranges: List[int]) -> bool:
    if not ranges:
        return False

    for i in ranges:
        if i[0] < n < i[1]:
            return True

    return False
# end snippet match
