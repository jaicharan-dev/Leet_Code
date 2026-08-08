class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        dp = []
        for row in triangle:
            dp.append([0]*len(row))

        for c in range(len(triangle[n-1])):
            dp[n-1][c] = triangle[n-1][c]

        for r in range(n-2, -1, -1):
            for c in range(len(triangle[r])):
                dp[r][c] = min(dp[r+1][c], dp[r+1][c+1]) + triangle[r][c]
        
        return dp[0][0]