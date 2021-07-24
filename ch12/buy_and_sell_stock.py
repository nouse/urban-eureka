from typing import List


# start snippet wow
def max_profit(prices: List[int]) -> int:
    profit = 0
    stack = [prices[0]]
    for price in prices[1:]:
        # 如果price小于栈顶元素，说明打破了连续增长，把当前利润填入
        if price < stack[-1]:
            if len(stack) > 1:
                profit += stack[-1] - stack[0]
            stack = []

        # 否则进行入栈操作
        if len(stack) > 1:
            stack[-1] = price
        else:
            stack.append(price)
    # 循环结束后如果栈内还有值，补上最后的利润
    if len(stack) > 1:
        profit += stack[-1] - stack[0]
    return profit
# end snippet wow
