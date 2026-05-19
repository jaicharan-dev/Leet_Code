class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []

        pac_set, atl_set = set(), set()
        pac_q, atl_q = deque(), deque() 
        rows, cols = len(heights), len(heights[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        for c in range(cols):
            pac_q.append((0, c))
            pac_set.add((0, c))
            atl_q.append((rows-1, c))
            atl_set.add((rows-1, c))
        
        for r in range(rows):
            pac_q.append((r, 0))
            pac_set.add((r, 0))
            atl_q.append((r, cols-1))
            atl_set.add((r, cols-1))

        while pac_q:
            r, c = pac_q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0 <= nr < rows) and (0 <= nc < cols) and heights[nr][nc] >= heights[r][c]:
                    if (nr,nc) not in pac_set:
                        pac_set.add((nr, nc))
                        pac_q.append((nr,nc))

        while atl_q:
            r, c = atl_q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0 <= nr < rows) and (0 <= nc < cols) and heights[nr][nc] >= heights[r][c]:
                    if (nr,nc) not in atl_set:
                        atl_set.add((nr, nc))
                        atl_q.append((nr,nc))
        
        return [list(cell) for cell in (pac_set & atl_set)]