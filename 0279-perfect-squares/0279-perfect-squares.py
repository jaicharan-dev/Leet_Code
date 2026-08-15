class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        i = 1 
        while i*i <= n:
            perfect_squares.append(i*i)
            i += 1
        
        dp = [float("inf")] * (n+1)
        dp[0] = 0

        for a in range(1, n+1):
            for s in perfect_squares:
                if a - s >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-s])
        
        return dp[n] if dp[n] != float("inf") else -1