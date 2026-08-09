# from functools import cache
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        memo = [[[-1] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        def dfs(r, c, moves_left):
            if r < 0 or r == m or c < 0 or c == n:
                return 1
            if moves_left == 0:
                return 0
            
            if memo[r][c][moves_left] != -1:
                return memo[r][c][moves_left]
            
            total_paths = 0
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                total_paths = (total_paths + dfs(r+dr, c+dc, moves_left-1)) % MOD

            memo[r][c][moves_left] = total_paths
            return total_paths

        return dfs(startRow, startColumn, maxMove)
