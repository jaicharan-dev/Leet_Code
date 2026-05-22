class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Counts the total number of distinct islands in a 2D binary grid.

        --- ALGORITHM STRATEGY: DESTALINIZATION / IN-PLACE SINKING VIA DFS ---
        We scan the grid cell-by-cell. When we find a piece of land ('1'), it represents 
        the discovery of a brand-new island, so we increment our count.

        To ensure we don't accidentally recount different sections of this same island, 
        we immediately deploy a Depth-First Search (DFS) from that cell. The DFS acts 
        like a virus, spreading to all 4 adjacent directions (Up, Down, Left, Right). 
        
        As the DFS visits each connected land cell, it "sinks" it by modifying its value 
        in-place from '1' to '0' (water). This clever modification handles two things:
        1. It serves as our 'visited' tracking mechanism, preventing infinite loops.
        2. It wipes the island off the grid map so our main loop won't discover it again.

        --- TIME & SPACE COMPLEXITY ---
        - Time Complexity: O(R * C), where R is rows and C is columns. Every single cell 
          is checked by the main loop. Land cells are visited by the DFS exactly once 
          because they are turned to water immediately upon being processed.
        - Space Complexity: O(R * C) in the worst-case scenario. If the entire grid is 
          one giant piece of land, the implicit recursion stack will grow to the size 
          of the grid.
        """
        
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        islands_count = 0

        # here is our virus
        def dfs(r, c):
            
            if not (0 <= r < rows) or not (0 <= c < cols) or grid[r][c] == "0":
                return
                
            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands_count += 1
                    dfs(r, c)
        
        return islands_count

        # check if grid exists to count islands
        # get the dimensions of the grid
        # the dfs function is to check if the current section is
        # not out of bounds and if its a land
        # the function is like a virus
        # spreads to all the connected pieces and sinks them for good
        # so that they are no counted again for a different island
            # check boundaries, and if its a land
            # if not a land or out of bounds, then nothing to do
            # if its a land then sink it
            # check in all 4 directions
        # traverse the full grid to find islands and keep a count of it
            # finally return the count
        