from typing import List


# start snippet init
def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    rows = len(matrix)
    columns = len(matrix[0])
    cache = {}
    # end snippet init

    # start snippet dps
    def dps(m: int, n: int) -> int:
        # 如果该单元格已经遍历过，直接返回对应的值
        if (m, n) in cache:
            return cache[(m, n)]

        # 上下左右四个方向的相邻单元格
        adjs = [(m + 1, n), (m - 1, n), (m, n + 1), (m, n - 1)]
        choices = [(i, j) for i, j in adjs
                   # 相邻的单元格需要在矩阵范围内，且比当前单元格小
                   if 0 <= i < rows and 0 <= j < columns and\
                   matrix[i][j] < matrix[m][n]]
        if not choices:
            return 1
        # 使用dps方法访问比当前单元格小的相邻的单元格
        # 因为使用了哈希表，不会造成函数调用栈溢出
        r = max([dps(i, j) for (i, j) in choices]) + 1
        # 存储当前单元格的返回值到哈希表
        cache[(m, n)] = r
        return r
    # end snippet dps

    # start snippet loop
    for i in range(rows):
        for j in range(columns):
            dps(i, j)

    return max(cache.values())
    # end snippet loop
