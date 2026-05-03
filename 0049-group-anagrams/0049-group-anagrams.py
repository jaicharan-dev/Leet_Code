class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)
        for word in strs:
            freqMap = [0] * 26
            for char in word:
                freqMap[ord(char) - ord('a')] += 1

            wordMap[tuple(freqMap)].append(word)
        return list(wordMap.values())
