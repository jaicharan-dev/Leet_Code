class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [[0] * n for _ in range(n)]

        for c in range(n):
            dp[0][c] = matrix[0][c]
        
        for r in range(1, n):
            for c in range(n):
                left = dp[r-1][c-1] if c > 0 else float("inf")
                top = dp[r-1][c]
                right = dp[r-1][c+1] if c < n-1 else float("inf")

                dp[r][c] = matrix[r][c] + min(left, top, right)

        return min(dp[n-1])