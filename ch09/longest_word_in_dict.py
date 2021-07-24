from typing import List


# start snippet init
def longest_word(words: List[str]) -> str:
    if not words:
        return ""

    buckets = [set() for i in range(30)]
    for word in words:
        buckets[len(word) - 1].add(word)
    # end snippet init
    # start snippet loop
    for i in range(29, 0, -1):
        # 使用sorted对set进行字典序排序
        for word in sorted(buckets[i]):
            for j in range(i, 0, -1):
                # 判断word[0:j]是否在对应的“桶”之中
                # 否则中止循环
                if word[0:j] not in buckets[j-1]:
                    break
            # else语句对应循环没有中止的情况
            # 循环正确结束则说明当前字符串满足条件
            else:
                return word
    return sorted(buckets[0])[0]
    # end snippet loop
