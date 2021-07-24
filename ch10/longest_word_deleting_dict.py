from bisect import bisect_right
from typing import List


# start snippet init
def find_longest_word(s: str, d: List[str]) -> str:
    m = {}
    for i, c in enumerate(s):
        if c in m:
            m[c].append(i)
        else:
            m[c] = [i]

    r = ""
    for entry in d:
        if ((len(entry) == len(r) and entry < r)
                or len(entry) > len(r)) and match(m, entry):
            r = entry
    return r
    # end snippet init


# start snippet match
def match(m: dict, p: str) -> bool:
    index = -1
    for c in p:
        indices = m.get(c, [])
        if not indices:
            return False
        # 使用二分查找，查找下一个比当前下标大的值
        bi = bisect_right(indices, index)
        if bi >= len(indices):
            return False
        # 更新当前下标
        index = indices[bi]
    return True
# end snippet match
