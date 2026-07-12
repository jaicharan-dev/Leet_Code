class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i in memo: return memo[i]
            if i == len(s): return True

            for word in wordDict:
                if word == s[i:i+len(word)]:
                    if dfs(i+len(word)):
                        memo[i] = True
                        return True
                    
            memo[i] = False
            return False

        return dfs(0)