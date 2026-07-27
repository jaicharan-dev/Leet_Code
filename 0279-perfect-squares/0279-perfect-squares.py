class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            for s in squares:
                if i-s >= 0:
                    dp[i] = min(dp[i], 1+dp[i-s])

        return dp[-1]