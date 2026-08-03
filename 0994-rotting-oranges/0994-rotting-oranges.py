class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and fresh:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (not 0 <= nr < rows or
                        not 0 <= nc < cols or
                        grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
        return time if fresh == 0 else -1


