class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for element in path.split('/'):
            if element == "..":
                if stack:
                    stack.pop()
            elif element in (".", ""):
                continue
            else:
                stack.append(element)
        return '/' + '/'.join(stack)