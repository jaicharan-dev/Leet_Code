class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freqMap1 = [0] * 26        
        freqMap2 = [0] * 26

        for i in range(len(s1)):
            freqMap1[ord(s1[i]) - ord('a')] += 1
            freqMap2[ord(s2[i]) - ord('a')] += 1
        
        if freqMap1 == freqMap2:
            return True
        
        for j in range(len(s1), len(s2)):
            i = j - len(s1)
            freqMap2[ord(s2[i]) - ord('a')] -= 1
            freqMap2[ord(s2[j]) - ord('a')] += 1
            
            if freqMap1 == freqMap2:
                return True
        
        return False

 