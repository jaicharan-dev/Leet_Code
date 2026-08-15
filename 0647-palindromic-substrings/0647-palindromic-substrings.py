class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    total_count += 1
                    l -= 1
                    r += 1
                else:
                    break
            
            l, r = i, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    total_count += 1
                    l -= 1
                    r += 1
                else:
                    break
        
        return total_count

            