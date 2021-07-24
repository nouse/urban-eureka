from typing import List


# start snippet wow
def trap(height: List[int]) -> int:
    # LTR: 从左向右
    # RTL: 从右向左
    ltr, rtl, total, max_ltr, max_rtl = 0, 0, 0, 0, 0
    for i, h in enumerate(height):
        max_ltr = max(max_ltr, h)
        # 计算图12.9中黑色部分面积
        ltr += max_ltr
        # 计算图12.8中黑色部分面积
        total += h

        reversed_i = len(height) - 1 - i
        max_rtl = max(max_rtl, height[reversed_i])
        # 计算图12.10中黑色部分面积
        rtl += max_rtl

    return ltr + rtl - max_ltr*len(height) - total
# end snippet wow
