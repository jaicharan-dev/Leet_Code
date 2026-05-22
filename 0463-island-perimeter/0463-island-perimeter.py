class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Calculates the perimeter of the single island in the grid using Depth-First Search (DFS).
        
        --- ALGORITHM STRATEGY: GRAPH TRAVERSAL WITH EARLY EXIT ---
        The standard iterative approach scans every single cell in the grid, which 
        wastes time checking empty water cells. Since the problem guarantees there 
        is exactly ONE island, we can optimize this:
        
        1. Scan the grid line-by-line until we hit our very first piece of land (1).
        2. From that starting coordinate, launch a DFS to traverse and map the entire island.
        3. Once the DFS is complete, we immediately return the perimeter and exit the function, 
           completely bypassing the rest of the grid.

        --- CRITICAL MECHANIC: PREVENTING INFINITE RECURSION ---
        In a graph traversal, neighboring land cells point to each other. Without a 
        tracking system, the DFS would infinitely bounce back and forth between adjacent 
        land blocks (e.g., cell A calls cell B, cell B calls cell A) until a stack overflow occurs.
        
        To prevent this, we modify the grid in place: when we land on a cell, we change its value 
        from `1` to `-1` (Visited). If the DFS encounters `-1` later, it knows it has already 
        processed that land and turns back safely.

        --- TIME & SPACE COMPLEXITY ---
        - Time Complexity: 
          - Best Case: O(K) where K is the number of cells in the island. If the island is 
            located at the top-left, we explore it and exit immediately, skipping thousands of cells.
          - Worst Case: O(R * C) if we have to scan through water to find the island at the very 
            bottom-right, or if the island takes up the entire grid.
        - Space Complexity: O(K) auxiliary space required by the recursion stack to maintain 
          the active DFS path across the island.
        """
        
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        def dfs(r,c):
            nonlocal perimeter
            if not (0 <= r < rows) or not (0 <= c < cols) or grid[r][c] == 0:
                perimeter += 1
                return
            if grid[r][c] == -1:
                return
            grid[r][c] = -1
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                dfs(r+dr, c+dc)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r,c)
                    return perimeter
        return perimeter # not needed ( as we are gaurenteed there will be one island )


        # since there exists only one island
        # i think its waste to scan every single cell
        # i feel its better to find one part of the island and just explore the entire island
        # we can do this using a dfs
        # since there is only 1 island, we save from check all the cells
        # to add perimeter, we can explore each land in 4 directions,
        # in each direction
        # if its connected to land do nothing
        # if connected to water or border - add one 
        # here is a function to help us increment our perimeter
        # not sure if this dfs in its true sense
        # we use directions for bfs generally
        # first we check if the section is a land
        # if its a land - we check its 4 sides for "not land" to increment
        # if its water we return false, which can be used by the previous dfs
        # if any that is, to increment the perimeter
        # while we are looping 2 times which makes it O(n^2)
        # that only happens in one case, if the island is the last cell only
        # for everything else this method is quite good as it checks only for the first cells
        # then we skip everything else
        # the standard method is a O(n^2 is all the cases)
        # this approach ins a O(n^2) only in the worst case