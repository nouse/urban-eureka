def is_interleave(s1: str, s2: str, s3: str) -> bool:
    m = len(s1)
    n = len(s2)
    if m + n != len(s3):
        return False
    if m == 0:
        return s2 == s3
    if n == 0:
        return s1 == s3

    # start snippet init
    dp = [[False] * (n+1) for i in range(m+1)]
    # 填写第一行的值
    for j in range(n):
        if s3[j] != s2[j]:
            break
        dp[0][j + 1] = True
    # 填写第一列的值
    for i in range(m):
        if s3[i] != s1[i]:
            break
        dp[i + 1][0] = True
    # end snippet init

    # start snippet loop
    for i in range(m):
        for j in range(n):
            # s3的第i+j+1个字符是否等于s1的第i+1个字符，
            # 或者s2的第j+1个字符
            if (dp[i][j + 1] and s3[i + j + 1] == s1[i]) or \
                    (dp[i + 1][j] and s3[i + j + 1] == s2[j]):
                dp[i + 1][j + 1] = True

    return dp[m][n]
    # end snippet loop
