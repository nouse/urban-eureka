from typing import List


# start snippet init
def gna(n: int, paths: List[List[int]]) -> List[int]:
    # 从paths得到每个节点的相邻节点
    d = [[] for _ in range(n)]
    # 节点大的排在前面
    for path in paths:
        n, m = max(path), min(path)
        d[n - 1].append(m)
    s = {1, 2, 3, 4}
    # end snippet init

    # start snippet loop
    result = [1] * n
    for i in range(n):
        used = {result[j - 1] for j in d[i]}
        if not used:
            next
        result[i] = sorted(s - used)[0]
    return result
    # end snippet loop
