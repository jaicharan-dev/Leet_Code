class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                res = num1 + num2
                stack.append(res)
            elif token == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                res = num1 - num2
                stack.append(res)
            elif token == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                res = num1 * num2
                stack.append(res)
            elif token == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                res = int(num1/num2)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]
