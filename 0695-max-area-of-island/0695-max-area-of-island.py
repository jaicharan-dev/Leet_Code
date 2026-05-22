class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Finds the maximum area of any connected island in a 2D binary grid.

        --- ALGORITHM STRATEGY: RECURSIVE AGGREGATION VIA SINKING DFS ---
        This problem builds directly on top of the "Number of Islands" framework. 
        Instead of merely tracking *how many* islands exist, we need to find 
        the *size* (number of connected land cells) of each individual island.

        We sweep the grid cell-by-cell. When we find an unvisited land block (1):
        1. We launch a DFS to calculate the full area of this specific island.
        2. To compute area recursively, each active land cell contributes a value of 1 
           and queries its 4 cardinal neighbors (Down, Up, Right, Left).
        3. As the DFS hits water or grid boundaries, those endpoints return 0. The 
           accumulated results filter back up the call stack to give us the final area.
        4. Like before, we "sink" the land in-place (grid[r][c] = 0) to prevent 
           infinite recursion loops and to wipe it from future main loop searches.
        5. We compare this island's total mass against our running 'max_area'.

        --- TIME & SPACE COMPLEXITY ---
        - Time Complexity: O(R * C), where R is rows and C is columns. Every single cell 
          is examined by the nested loops. Each land cell is processed by the DFS exactly 
          once because it transitions into water immediately upon discovery.
        - Space Complexity: O(R * C) auxiliary space needed in the absolute worst-case 
          scenario (e.g., a grid completely filled with land), where the entire map 
          is stored on the implicit recursion call stack.
        """

        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        # here is our virus
        def dfs(r, c):
            if not (0 <= r < rows) or not (0  <= c < cols) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return ( 1 +
                dfs(r+1, c) +
                dfs(r-1, c) +
                dfs(r, c+1) +
                dfs(r, c-1)
            )
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))

        return max_area
        

        # if the grid does not exist then return 0
        # as the max area is 0
        # note the dimensions of the grid
        # use a global max variable
        # the dfs is like a virus, it checks the full area 
        # and simultaneously sinks the land
            # check boundary and for water
            # if its out of grid or water
            # then we do nothing
            # if its land, then
            # we sink the land, so its not used again
            # and we increment the area of the current land
            # and simultaneously check for of neighboring lands if any
            # this is recursion stack
        # iterate through all the grid points to search for land
                # if land found spread the virus and get your count 
                    # check the cur_area with the max area already found
        # return the max area after exploring all the lands

        
