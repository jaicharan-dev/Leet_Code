class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""

        target_dict = Counter(t)
        need = len(target_dict)

        curr_dict = {char:0 for char in target_dict.keys()}
        have = 0

        res_length = float("inf")
        res_start = 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in curr_dict:
                curr_dict[char] += 1
                if curr_dict[char] == target_dict[char]:
                    have += 1
                
            while have == need:
                if res_length > (right-left+1):
                    res_start = left
                    res_length = right-left+1
                
                left_char = s[left]
                if left_char in curr_dict:
                    curr_dict[left_char] -= 1
                    if curr_dict[left_char] < target_dict[left_char]:
                        have -= 1
                
                left += 1
        return s[res_start:res_start+res_length] if res_length != float('inf') else ""
        