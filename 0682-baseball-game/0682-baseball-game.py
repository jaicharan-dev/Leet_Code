class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == "C":
                stack.pop()
            
            elif operation == "D":
                stack.append(int(stack[-1]) * 2)
                
            elif operation == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))

            else:
                stack.append(int(operation))

        return sum(stack)