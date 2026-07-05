class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = ""
        for char in s:
            if char.isnumeric():
                curr_num += char
            elif char == "[":
                stack.append(curr_str)
                curr_str = ""
                stack.append(int(curr_num))
                curr_num = ""
            elif char == "]":
                number = stack.pop()
                prev_char = stack.pop()
                curr_str = prev_char + number * (curr_str)
            else:
                curr_str += char
                
        return curr_str