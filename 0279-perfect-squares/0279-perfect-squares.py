class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        
        dp = [float("inf")] * (n+1)
        dp[0] = 0

        for a in range(1, n+1):
            for sq in squares:
                if a - sq >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-sq])
                else:
                    break

        return dp[n]