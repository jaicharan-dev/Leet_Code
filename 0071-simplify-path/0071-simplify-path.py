class Solution:
    def simplifyPath(self, path: str) -> str:
        raw_data = path.split('/')
        stack = []
        for data in raw_data:
            if data == "" or data == ".":
                continue
            elif data == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(data)
        return "/" + "/".join(stack)