class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ""

        char_map = [0] * 128
        for char in t:
            char_map[ord(char)] += 1
        
        left = 0
        count = len(t)
        min_start = 0
        min_len = float('inf')

        for right in range(len(s)):
            if char_map[ord(s[right])] > 0:
                count -= 1 
            char_map[ord(s[right])] -= 1
            
            while count == 0:
                if right-left+1 < min_len:
                    min_len = right-left+1
                    min_start = left
                
                char_map[ord(s[left])] += 1
                if char_map[ord(s[left])] > 0:
                    count += 1
                left += 1
        
        return "" if min_len == float('inf') else s[min_start : min_start + min_len]
            

        
