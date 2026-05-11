class Solution:
    def isValid(self, s: str) -> bool:
        dictMap = { ")" : "(", "}" : "{", "]" : "[" }
        stack = []

        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if prev != dictMap[bracket]:
                    return False
        
        return True if not stack else False


