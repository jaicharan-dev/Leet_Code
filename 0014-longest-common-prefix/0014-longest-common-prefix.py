class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        prefix_word = min(strs)
        for i in range(len(prefix_word)):
            char = prefix_word[i]
            for word in strs:
                if word[i] != char:
                    return res
            res += char
        
        return res

            
