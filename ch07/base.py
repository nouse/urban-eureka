def base(n: int, k: int) -> str:
    q, r = divmod(n, k)
    a = [str(r)]
    while q > k:
        q, r = divmod(q, k)
        a.append(str(r))
    a.append(str(q))
    return "".join(reversed(a))
