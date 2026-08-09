class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if not (0 <= r < m) or not (0 <= c < n) or grid[r][c] == 0:
                return 0
            
            current_gold = grid[r][c]
            grid[r][c] = 0

            max_from_neighbors = 0
            directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                max_from_neighbors = max(max_from_neighbors, dfs(r+dr, c+dc))            
            grid[r][c] = current_gold

            return current_gold + max_from_neighbors
                
        max_gold = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    max_gold = max(max_gold, dfs(r, c))
            
        return max_gold


