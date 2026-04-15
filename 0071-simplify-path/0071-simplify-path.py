class Solution:
    def simplifyPath(self, path: str) -> str:
        elements = path.strip('/').split('/')
        stack = []
        for element in elements:
            if element == "..":
                if stack:
                    stack.pop()
            elif element == ".":
                continue
            elif element == "":
                continue
            else:
                stack.append(element)
        return '/' + '/'.join(stack)