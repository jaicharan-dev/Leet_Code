class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac_set, atl_set = set(), set()

        def dfs(r, c, visit_set, prev_height):
            if (not (0 <= r < rows) or
                not (0 <= c < cols) or
                (r,c) in visit_set or
                heights[r][c] < prev_height):
                return

            visit_set.add((r,c))

            dfs(r+1,c, visit_set, heights[r][c]) 
            dfs(r-1,c, visit_set, heights[r][c]) 
            dfs(r,c+1, visit_set, heights[r][c]) 
            dfs(r,c-1, visit_set, heights[r][c]) 
            return

        for r in range(rows):
            dfs(r, 0, pac_set, 0)
            dfs(r, cols-1, atl_set, 0)
        
        for c in range(cols):
            dfs(0, c, pac_set, 0)
            dfs(rows-1, c, atl_set, 0)
        
        res = []
        for (r,c) in pac_set & atl_set:
            res.append([r,c])
        
        return res
