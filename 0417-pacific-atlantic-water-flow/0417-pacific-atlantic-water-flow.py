class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac_set, atl_set = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, ocean_set, prev_height):

            if (not (0 <= r < rows) or
                not (0 <= c < cols) or 
                prev_height > heights[r][c] or
                (r,c) in ocean_set):
                return 
            
            ocean_set.add((r,c))

            dfs(r+1, c, ocean_set, heights[r][c])
            dfs(r-1, c, ocean_set, heights[r][c])
            dfs(r, c+1, ocean_set, heights[r][c])
            dfs(r, c-1, ocean_set, heights[r][c])
            return
        
        for r in range(rows):
            dfs(r, 0, pac_set, 0)
            dfs(r, cols-1, atl_set, 0)
        
        for c in range(cols):
            dfs(0, c, pac_set, 0)
            dfs(rows-1, c, atl_set, 0)
        
        return list(pac_set & atl_set)

        
        

