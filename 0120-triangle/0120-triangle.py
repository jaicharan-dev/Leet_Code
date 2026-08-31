class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        dp = []
        for r in range(1, n+1):
            dp.append([0] * r)
        
        for c in range(n):
            dp[n-1][c] = triangle[n-1][c]
        
        for r in range(n-2,-1,-1):
            for c in range(r+1):
                dp[r][c] = triangle[r][c] + min(dp[r+1][c], dp[r+1][c+1])

        return dp[0][0]