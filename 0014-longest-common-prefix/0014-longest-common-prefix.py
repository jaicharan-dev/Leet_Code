class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        first_word = strs[0]
        for i in range(len(first_word)):
            for other_word in strs[1:]:
                if i == len(other_word) or first_word[i] != other_word[i]:
                    return first_word[:i]
        return first_word
