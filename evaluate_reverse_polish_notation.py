class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
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
        # assert (len(stack) == 1)
        return stack[0]
