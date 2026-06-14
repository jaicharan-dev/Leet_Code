class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strs:
            freq_map = [0] * 26  
            for char in s:
                freq_map[ord(char) - ord('a')] += 1  
            hash_map[tuple(freq_map)].append(s)

        res = [char_list for char_list in hash_map.values()]
        return res