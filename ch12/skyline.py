from typing import List
from bisect import bisect, insort


def get_skyline(buildings: List[List[int]]) -> List[List[int]]:
    # start snippet init
    result = []
    stack = []
    height_of_stack = 0
    # end snippet init

    # start snippet draw
    # 从start下标开始从右向左绘制天际线
    def draw_skyline(start: int, max_height: int):
        tail = []
        for i in range(start, -1, -1):
            if (item := stack.pop(i))[1] > max_height:
                if len(tail) > 0 and tail[-1][0] == item[0]:
                    tail[-1][1] = max_height
                else:
                    tail.append([item[0], max_height])
                max_height = item[1]
        result.extend(reversed(tail))
    # end snippet draw

    # start snippet loop
    for building in buildings:
        # 查找当前点在未结束建筑物数组的位置
        index = bisect(stack, (building[0], 0))
        # 如果不为0，说明当前点左侧有需要绘制天际线的建筑物
        if index != 0:
            # 根据尚未结束的建筑物计算最大高度
            height_of_stack = max([s[1] for s in stack[index:]],
                                  default=0)
            draw_skyline(index - 1, height_of_stack)

        height = building[2]
        # 如果当前建筑物没有被覆盖，需要加入结果变量
        if height > height_of_stack:
            if len(result) > 0 and result[-1][0] == building[0]:
                result[-1][1] = height
            else:
                result.append([building[0], height])
            height_of_stack = height

        # 将当前建筑物加入尚未结束建筑物的数组
        insort(stack, (building[1], height))
    # 最后一次绘制天际线
    draw_skyline(len(stack) - 1, 0)
    return result
    # end snippet loop
