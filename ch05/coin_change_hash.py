from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    # start snippet wow
    # 使用哈希表，只需要初始化总额为0的情况
    solutions = {0: 0}

    for i in range(1, amount + 1):
        # 减去每种零钱的面值，查找哈希表，列出所有的可能值
        candidates = [
            solutions[i - coin]
            for coin in coins
            if i >= coin and i - coin in solutions]

        if candidates:
            solutions[i] = min(candidates) + 1

    return solutions.get(amount, -1)
    # end snippet wow
