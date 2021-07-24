# start snippet init
def length_of_longest_substring(s: str) -> int:
    d = {}  # 字符 => 上一次出现的位置
    longest = 0  # 全局最长的无重复子串长度
    start = -1  # 重复字符上一次出现的位置
    # end snippet init
    # start snippet loop
    for i, c in enumerate(s):
        # 如果出现了重复字符，且大于上次出现的位置，
        # 需要重新计算当前最长的无重复子串长度
        if c in d and d[c] > start:
            longest = max(longest, i-start-1)
            start = d[c]
        d[c] = i
    # 结束循环后，再次更新全局最长的无重复子串长度
    return max(longest, len(s)-start-1)
    # end snippet loop
