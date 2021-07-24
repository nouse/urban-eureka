BASE = 29
BIG_PRIME = 100_000_000_7


# start snippet init
def longest_prefix(s: str) -> str:
    n = len(s)
    longest = ""
    prefix = code(s[0])
    suffix = code(s[-1])
    # 底数的n-1次幂
    power = 1
    # end snippet init

    # start snippet loop
    for i in range(1, n):
        # 如果当前前缀等于当前后缀，更新最长开心前缀为当前前缀
        if prefix == suffix and s[0:i] == s[n-i:]:
            longest = s[0:i]
        prefix = (prefix * BASE + code(s[i])) % BIG_PRIME
        power = (power * BASE) % BIG_PRIME
        suffix = (code(s[n-i-1]) * power + suffix) % BIG_PRIME

    return longest
    # end snippet loop


def code(s: str) -> int:
    return ord(s) - 96  # 'a' ascii code is 97
