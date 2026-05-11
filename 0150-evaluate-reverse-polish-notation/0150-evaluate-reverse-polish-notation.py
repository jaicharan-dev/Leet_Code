class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token == "+":
                temp2 = stack.pop()
                temp1 = stack.pop()
                stack.append(temp1 + temp2)
            
            elif token == "-":
                temp2 = stack.pop()
                temp1 = stack.pop()
                stack.append(temp1 - temp2)
            
            elif token == "*":
                temp2 = stack.pop()
                temp1 = stack.pop()
                stack.append(temp1 * temp2)
            
            elif token == "/":
                temp2 = stack.pop()
                temp1 = stack.pop()
                stack.append(int(temp1 / temp2))
            
            else:
                stack.append(int(token))

        return stack.pop()