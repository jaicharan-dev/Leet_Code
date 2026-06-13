class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count_island = 0

        def dfs(r, c):
            if (not (0 <= r < rows) or not (0 <= c < cols) or
                grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            return
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count_island += 1
                    dfs(r,c)
        return count_island

