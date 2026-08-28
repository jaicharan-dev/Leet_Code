class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]

        for r in range(m):
            if obstacleGrid[r][0] == 1:
                break
            dp[r][0] = 1
        
        for c in range(n):
            if obstacleGrid[0][c] == 1:
                break
            dp[0][c] = 1

        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
            
        return dp[m-1][n-1]
