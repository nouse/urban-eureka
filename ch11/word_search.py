from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    if not board:
        return False

    d = {}
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c in d:
                d[c].append((i, j))
            else:
                d[c] = [(i, j)]

    searched = {}

    def dfs(m, n, i) -> bool:
        if i == len(word):
            return True
        searched[(m, n)] = True
        for nchoice in d.get(word[i], []):
            if not searched.get(nchoice, False) and\
                    adjacent(nchoice, (m, n)) and\
                    dfs(nchoice[0], nchoice[1], i + 1):
                return True
        searched[(m, n)] = False
        return False

    for i, j in d.get(word[0], []):
        if dfs(i, j, 1):
            return True
    return False


def adjacent(p1, p2):
    return (abs(p1[0] - p2[0]) == 1 and p1[1] == p2[1]) or \
           (p1[0] == p2[0] and abs(p1[1] - p2[1]) == 1)
