class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        res = []
        for i in range(min_len):
            res.append(word1[i])
            res.append(word2[i])
        
        res.append(word1[min_len:])
        res.append(word2[min_len:])
        
        return "".join(res)

