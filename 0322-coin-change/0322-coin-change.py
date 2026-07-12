class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i):
            if i in memo: return memo[i]
            if i == 0: return 0
            if i < 0: return float("inf")

            min_cnt = float("inf")
            for c in coins:
                curr_cnt = 1 + dfs(i-c) 
                min_cnt = min(min_cnt, curr_cnt)

            memo[i] = min_cnt
            return memo[i]

        result = dfs(amount)
        return result if result != float("inf") else -1
