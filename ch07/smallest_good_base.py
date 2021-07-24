# start snippet good_base
def good_base(n: int, k: int) -> bool:
    q, r = divmod(n, k)
    if r != 1:
        return False
    while q > 0:
        q, r = divmod(q, k)
        if r != 1:
            return False
    return True
# end snippet good_base


# start snippet smallest_good_base
def smallest_good_base(n: str) -> str:
    n = int(n)
    for k in range(2, n - 1):
        if good_base(n, k):
            return str(k)
    return str(n - 1)
# end snippet smallest_good_base
