class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        s_map = [0] * 26
        t_map = [0] * 26

        for i in range(len(s)):
            s_map[ord(s[i]) - ord('a')] += 1
            t_map[ord(t[i]) - ord('a')] += 1

        return s_map == t_map        
            