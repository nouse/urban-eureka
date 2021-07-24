from typing import List


# start snippet init
def exist(board: List[List[str]], word: str) -> bool:
    if not board:
        return False

    rows = len(board)
    columns = len(board[0])
    # 保存已访问的单元格
    searched = set()
    # end snippet init

    # start snippet dfs
    def dfs(m, n, l) -> bool:
        # 如果已经达到给定单词的结尾，返回True
        if l == len(word):
            return True

        # 将当前单元格加入已访问集合
        searched.add((m, n))
        for i, j in [(m+1, n), (m-1, n), (m, n+1), (m, n-1)]:
            # 单元格不超出表格范围
            if 0 <= i < rows and 0 <= j < columns and (
                # 单元格没有被搜索
                not (i, j) in searched) and (
                # 单元格等于下一个字符，进行下一步深度优先遍历
                    board[i][j] == word[l] and dfs(i, j, l+1)):
                return True
        # 结束当前单元格的访问，从已访问集合中删除
        searched.remove((m, n))
        return False
    # end snippet dfs

    # start snippet loop
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == word[0] and dfs(i, j, 1):
                return True
    return False
    # end snippet loop
