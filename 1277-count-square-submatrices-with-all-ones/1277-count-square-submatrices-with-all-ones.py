class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        total_squares = 0

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1
                    
                    total_squares += dp[r][c]

        return total_squares
