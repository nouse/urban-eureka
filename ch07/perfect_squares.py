# start snippet init
def num_squares(n: int) -> int:
    result = [1] * (n + 1)
    squares = [1]
    next_root = 2
    next_square = 4
    # end snippet init

    # start snippet loop
    for i in range(2, n + 1):
        if i == next_square:
            # 更新相应的变量
            squares.append(next_square)
            next_root += 1
            next_square = next_root ** 2
            continue
        # end snippet loop
        # start snippet next
        # 如果当前的值不等于下一个平方数，找出所有的可能值然后取最小值。
        result[i] = min([result[i - j] for j in squares]) + 1
        # end snippet next
    return result[n]
