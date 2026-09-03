class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((0,1), (0,-1), (1,0), (-1,0))

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            curr_gold = grid[r][c]
            grid[r][c] = 0
            
            neighbor_gold = 0
            for dr, dc in directions:
                neighbor_gold = max(neighbor_gold, dfs(r+dr, c+dc))
            
            grid[r][c] = curr_gold
            
            return curr_gold + neighbor_gold

        max_gold = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    max_gold = max(max_gold, dfs(r,c))

        return max_gold
                
                