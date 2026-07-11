class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i):
            if i in memo: return memo[i]
            if i == 0: return 0
            min_cnt = float("inf")

            for coin in coins:
                if i-coin < 0: continue
                coins_cnt = 1 + dfs(i-coin)
                min_cnt = min(min_cnt, coins_cnt)

            memo[i] = min_cnt
            return memo[i]

        result = dfs(amount)
        return result if result != float("inf") else -1