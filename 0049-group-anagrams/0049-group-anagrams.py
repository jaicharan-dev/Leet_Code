class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for word in strs:
            frequencyMap = [0] * 26
            for char in word:
                frequencyMap[ord(char) - ord('a')] += 1
            hashMap[tuple(frequencyMap)].append(word)
        
        return list(hashMap.values())
            