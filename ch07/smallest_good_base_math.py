import math


# start snippet gb
def good_base(n: int, k: int) -> bool:
    target = n*(k-1)+1
    # math.log返回满足k^power=target的值
    power = round(math.log(target, k))
    return k**power == target
# end snippet gb


# start snippet sgb
def smallest_good_base(n: str) -> str:
    n = int(n)
    # m满足 2^m < n < 2^(m+1)
    max_m = math.floor(math.log2(n))
    for m in range(max_m, 1, -1):
        # k满足 k^m < n < (k+1)^m
        k = math.floor(n ** (1 / m))
        # n = k^(m+1)-1 / k-1
        if n * (k - 1) + 1 == k ** (m + 1):
            return str(k)
    return str(n - 1)
# end snippet sgb
