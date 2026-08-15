class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = (0,0)

        for i in range(len(s)):
            l, r = i, i
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    if max_str[1] - max_str[0] < r - l + 1:
                        max_str = (l, r)
                    l -= 1
                    r += 1
                else:
                    break

            l, r = i, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if max_str[1] - max_str[0] < r - l + 1:
                        max_str = (l, r)
                    l -= 1
                    r += 1
                else:
                    break
            
        return s[max_str[0]:max_str[1]+1]