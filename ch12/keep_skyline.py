from typing import List


def max_increase_keeping_skyline(grid: List[List[int]]) -> int:
    # start snippet wow
    n = len(grid)
    m = len(grid[0])
    max_y = [max(grid[i]) for i in range(n)]
    max_x = [max([grid[i][j] for i in range(n)]) for j in range(m)]
    total = 0

    for i in range(n):
        for j in range(m):
            total += min(max_x[j], max_y[i]) - grid[i][j]
    return total
    # end snippet wow
