class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freqMap1 = [0] * 26        
        freqMap2 = [0] * 26

        for i in range(len(s1)):
            freqMap1[ord(s1[i]) - ord('a')] += 1
            freqMap2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if freqMap1[i] == freqMap2[i]:
                matches += 1


        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            incoming_idx = ord(s2[i]) - ord('a')
            freqMap2[incoming_idx] += 1
            
            if freqMap1[incoming_idx] == freqMap2[incoming_idx]:
                matches += 1
            if freqMap1[incoming_idx] + 1 == freqMap2[incoming_idx]:
                matches -= 1
            
            outgoing_idx = ord(s2[i-len(s1)]) - ord('a')
            freqMap2[outgoing_idx] -= 1

            if freqMap1[outgoing_idx] == freqMap2[outgoing_idx]:
                matches += 1
            if freqMap1[outgoing_idx] - 1 == freqMap2[outgoing_idx]:
                matches -= 1

        return matches == 26
