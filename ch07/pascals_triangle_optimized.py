from typing import List


# start snippet wow
def pascals_triangle(n: int) -> List[int]:
    a = [1] * (n + 1)

    for k in range(1, n):
        a[k] = a[k - 1] * (n + 1 - k) // k

    return a
# end snippet wow
