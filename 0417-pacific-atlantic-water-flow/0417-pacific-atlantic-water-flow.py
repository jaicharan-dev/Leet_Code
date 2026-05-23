class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return []
        
        pac_set, atl_set = set(), set()
        pac_q, atl_q = deque(), deque()
        rows, cols = len(heights), len(heights[0])

        for r in range(rows):
            pac_q.append((r,0))
            pac_set.add((r,0))
            atl_q.append((r,cols-1))
            atl_set.add((r,cols-1))
        
        for c in range(cols):
            if (0,c) not in pac_set:
                pac_q.append((0,c))
                pac_set.add((0,c))
            if (rows-1,c) not in atl_set:
                atl_q.append((rows-1,c))
                atl_set.add((rows-1,c))
        
        def bfs(queue, visit_set):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < rows and 0 <= nc < cols and 
                    (nr,nc) not in visit_set and heights[nr][nc] >= heights[r][c]):
                        queue.append((nr,nc))
                        visit_set.add((nr,nc))
        
        bfs(pac_q, pac_set)
        bfs(atl_q, atl_set)

        return [list(cell) for cell in (pac_set & atl_set)]



