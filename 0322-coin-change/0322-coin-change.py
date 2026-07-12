class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        return dp[amount] if dp[amount] != float("inf") else -1