from typing import List


# start snippet wow
def max_area(height: List[int]) -> int:
    left, right = 0, len(height)-1
    m = 0
    while left < right:
        if height[left] <= height[right]:
            m = max(m, height[left] * (right - left))
            left += 1
        else:
            m = max(m, height[right] * (right - left))
            right -= 1
    return m
# end snippet wow
