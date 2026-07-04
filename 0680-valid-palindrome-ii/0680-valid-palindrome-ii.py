class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                str1 = s[:left] + s[left+1:]
                str2 = s[:right] + s[right+1:]
                return self._is_pali(str1) or self._is_pali(str2)
            else:
                left += 1
                right -= 1
        return True
    
    def _is_pali(self, string):
        left, right = 0, len(string)-1
        while left < right:
            if string[left] != string[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
            