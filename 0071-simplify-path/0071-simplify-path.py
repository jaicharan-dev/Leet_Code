class Solution:
    def simplifyPath(self, path: str) -> str:
        string = path.split("/")
        stack = []

        for char in string:
            if char == '.' or char == '':
                continue
            elif char == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return "/" + "/".join(stack)
