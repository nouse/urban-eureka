def climb_stairs(n: int) -> int:
    a = [1] * (n + 1)
    a[2] = 2

    for i in range(3, n + 1):
        a[i] = a[i - 1] + a[i - 2] + a[i - 3]

    return a[n]
