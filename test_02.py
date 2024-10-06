def evalRPN(tokens: list[str]) -> int:
    stack = []
    res = 0
    for val in tokens:
        if val != "+" and val != "-" and val != "*" and val != "/":
            stack.append(int(val))
        else:
            after = stack.pop()
            before = stack.pop()
            if val == "+":
                result = before + after
                stack.append(result)
            elif val == "-":
                result = before - after
                stack.append(result)
            elif val == "*":
                result = before * after
                stack.append(result)
            elif val == "/":
                result = int(before / after)
                stack.append(result)
    assert (len(stack) == 1)
    return stack[0]


def nested_sum(l):
    total = 0  # don't use `sum` as a variable name
    for val in l:
        if isinstance(val, list):  # checks if `val` is a list
            total += nested_sum(val)
        else:
            total += val
    return total


def main() -> None:
    print(evalRPN(["10", "6", "9", "3", "+", "-11",
          "*", "/", "*", "17", "+", "5", "+"]))  # 22

    print(nested_sum([1, [2, [3, [4]], 5]]))  # 15


if __name__ == '__main__':
    main()
