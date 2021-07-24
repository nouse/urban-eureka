from typing import List


def max_profit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0
    # start snippet forward
    profits = [0] * len(prices)
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        price = prices[i]
        # 如果当前价格比最低价格低，更新最低价格
        if price < min_price:
            min_price = price
            profits[i] = max_profit
        else:
            max_profit = max(max_profit, price - min_price)
            profits[i] = max_profit
    # end snippet forward

    # start snippet backward
    max_profit = 0
    max_price = prices[-1]
    for i in range(len(prices), 2, -1):
        price = prices[i - 1]
        # 如果当前价格比最高价格高，更新最高价格
        if price > max_price:
            max_price = price
            profits[i - 2] += max_profit
        else:
            max_profit = max(max_profit, max_price - price)
            profits[i - 2] += max_profit

    return max(profits)
    # end snippet backward
