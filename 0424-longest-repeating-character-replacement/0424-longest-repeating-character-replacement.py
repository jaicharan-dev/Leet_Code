class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        left = 0
        length = 0

        for right in range(len(s)):
            freqMap[s[right]] = 1 + freqMap.get(s[right], 0)
            max_char = max(freqMap.values())

            while (right - left + 1) - max_char > k:
                freqMap[s[left]] -= 1
                left += 1

            length = max(length, (right - left + 1))
        
        return length
