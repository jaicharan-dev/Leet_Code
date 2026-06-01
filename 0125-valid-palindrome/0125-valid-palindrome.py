class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while not self.alphanum(s[l]) and l < r:
                l += 1
            while not self.alphanum(s[r]) and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1 
            r -= 1 

        return True

    def alphanum(self, c):
        if ord('a') <= ord(c) <= ord('z'): return True  
        if ord('A') <= ord(c) <= ord('Z'): return True  
        if ord('0') <= ord(c) <= ord('9'): return True
        return False  