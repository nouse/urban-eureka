from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    # start snippet start
    # 因为没有解需要返回-1，我们使用-1初始化数组
    solutions = [-1] * (amount + 1)
    # 总额为0则对应的个数为0
    solutions[0] = 0
    # end snippet start

    # start snippet wow
    for i in range(1, amount + 1):
        # 减去每种零钱的面值，查找数组，列出所有的可能值
        candidates = [
            solutions[i - coin]
            for coin in coins
            if i >= coin and solutions[i - coin] != -1]

        if candidates:
            solutions[i] = min(candidates) + 1

    return solutions[amount]
    # end snippet wow
