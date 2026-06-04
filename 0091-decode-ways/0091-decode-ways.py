class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        one_back = 1
        two_back = 1

        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current += one_back
            
            two_digit_val = int(s[i-1:i+1])

            if 10 <= two_digit_val <= 26:
                current += two_back
            
            two_back = one_back
            one_back = current
        
        return one_back
    
