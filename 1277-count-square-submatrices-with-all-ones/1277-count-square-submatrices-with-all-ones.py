class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        total_squares = 0

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    if r > 0 and c > 0:
                        matrix[r][c] = min(matrix[r-1][c], matrix[r-1][c-1], matrix[r][c-1]) + 1
                    
                    total_squares += matrix[r][c]
        
        return total_squares