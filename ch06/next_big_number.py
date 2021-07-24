from typing import List


# start snippet wow
def ng_ele(nums1: List[int], nums2: List[int]) -> List[int]:
    if not nums1:
        return []
    stack = [nums2[0]]
    d = {}
    for i in range(1, len(nums2)):
        n = nums2[i]
        while len(stack) > 0 and n > stack[-1]:  # 出栈操作
            d[stack.pop()] = n
        stack.append(n)  # 入栈操作

    for n in stack:
        d[n] = -1

    return [d[n] for n in nums1]
    # end snippet wow
