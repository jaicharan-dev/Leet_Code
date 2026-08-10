class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[[None] * n for _ in range(n)] for _ in range(m)]

        def dp(r, c1, c2):
            if not (0 <= c1 < n) or not (0 <= c2 < n):
                return float('-inf')
            
            if memo[r][c1][c2] is not None:
                return memo[r][c1][c2]
            
            if c1 == c2:
                curr_cherries = grid[r][c1]
            else:
                curr_cherries = grid[r][c1] + grid[r][c2]
            
            if r == m-1:
                memo[r][c1][c2] = curr_cherries
                return curr_cherries
            
            max_future = 0
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    max_future = max(max_future, dp(r+1, c1+dc1, c2+dc2))

            ans = curr_cherries + max_future
            memo[r][c1][c2] = ans
            return ans
        
        return dp(0, 0, n-1)
