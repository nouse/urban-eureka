# start snippet var
BASE = 29
BIG_PRIME = 100_000_000_7


def code(c: str) -> int:
    # "a"对应ASCII代码是97，输出值为1
    return ord(c) - 96
# end snippet var


# start snippet hash
def hash_code(s: str) -> int:
    v = 0
    for c in s:
        v = (v * BASE + code(c)) % BIG_PRIME
    return v
# end snippet hash


def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    # start snippet init
    # needle字符串的长度经常用到，保存为变量
    m = len(needle)
    # 计算needle和haystack第一个子串的散列值
    target = hash_code(needle)
    source = hash_code(haystack[0:m])
    # RM是底数的M次幂对于BIG_PRIME的余数
    remain = 1
    for _ in range(m):
        remain = (remain * BASE) % BIG_PRIME
    # end snippet init

    # start snippet wow
    if target == source and haystack[0:m] == needle:
        return 0
    for i in range(len(haystack) - m):
        # 进位，减去高位的余数，并加上低位对应的值，最后再取余数
        low = code(haystack[i + m])
        high = code(haystack[i])
        source = (source*BASE - high*remain + low) % BIG_PRIME
        if target == source and haystack[i+1:i+m+1] == needle:
            return i + 1
    return -1
    # end snippet wow
