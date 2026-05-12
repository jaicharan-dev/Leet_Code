class Solution:
    def simplifyPath(self, path: str) -> str:
        elements = path.split('/')
        stack = []
        for element in elements:
            if element == '':
                continue
            elif element == '.':
                continue            
            elif element == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(element)
    
        return '/' + '/'.join(stack)