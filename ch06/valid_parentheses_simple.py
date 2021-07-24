# start snippet wow
def is_valid(s: str) -> bool:
    stack = []
    for c in s:
        if c == "(":  # 1. 如果遇到左括号，进行入栈操作
            stack.append(c)
            continue

        if not stack:  # 3. 遇到不成对的右括号，直接返回False。
            return False

        stack.pop()  # 2. 如果遇到右括号，进行出栈操作

    # 4. 遍历结束后发现不成对的左括号，返回False。
    return stack == []
    # end snippet wow
