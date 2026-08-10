class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        memo = [[None] * n for _ in range(m)]

        def dfs(r, c):
            if r >= m or c >= n:
                return float('inf')
            
            if memo[r][c] is not None:
                return memo[r][c]
            
            if r == m-1 and c == n-1:
                req = max(1, 1 - dungeon[r][c])
                memo[r][c] = req
                return req
            
            right_req = dfs(r, c+1)
            down_req = dfs(r+1, c)

            min_next_req = min(right_req, down_req)
            req = max(1, min_next_req - dungeon[r][c])

            memo[r][c] = req
            return req
        
        return dfs(0, 0)