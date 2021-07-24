from typing import List


# start snippet wow
def pascals_triangle(n: int) -> List[int]:
    if n == 0:
        return [1]

    a = pascals_triangle(n - 1)
    a.append(1)
    for i in range(n, 1, -1):
        a[i - 1] += a[i - 2]
    return a
# end snippet wow
