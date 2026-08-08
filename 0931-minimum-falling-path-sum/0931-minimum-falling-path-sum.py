class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for c in range(n):
            dp[0][c] = matrix[0][c]
        
        for r in range(1, m):
            for c in range(n):
                top_left = dp[r-1][c-1] if c > 0 else float('inf')
                above = dp[r-1][c]
                top_right = dp[r-1][c+1] if c < n-1  else float('inf')
                
                dp[r][c] = matrix[r][c] + min(top_left, above, top_right)
            
        return min(dp[-1])