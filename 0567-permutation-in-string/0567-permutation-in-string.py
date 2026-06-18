class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(n1):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        
        if freq1 == freq2:
            return True
        
        for j in range(n1, n2):
            freq2[ord(s2[j]) - ord('a')] += 1
            freq2[ord(s2[j - n1]) - ord('a')] -= 1

            if freq1 == freq2:
                return True
            
        return False
        