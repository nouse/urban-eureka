# start snippet wow
def is_valid(s: str) -> bool:
    stack = []
    d = {"(": ")", "[": "]", "{": "}"}
    for c in s:
        if c in d:  # 如果是左括号，则把对应的右括号入栈
            stack.append(d[c])
            continue

        # 如果是不成对的右括号，或不是正确顺序的右括号，返回False
        if stack == [] or stack[-1] != c:
            return False

        stack.pop()  # 正确顺序的右括号，进行出栈操作

    return stack == []
    # end snippet wow
