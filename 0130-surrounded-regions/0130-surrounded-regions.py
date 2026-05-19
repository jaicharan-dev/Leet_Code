class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        queue = deque()

        for r in range(rows):
            if board[r][0] == "O":
                queue.append((r,0))
            if board[r][cols-1] == "O":
                queue.append((r,cols-1))
            
        for c in range(cols):
            if board[0][c] == "O":
                queue.append((0,c))
            if board[rows-1][c] == "O":
                queue.append((rows-1,c))
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while queue:
            r, c = queue.popleft()
            board[r][c] = "T"
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0 <= nr < rows) and (0 <= nc < cols) and board[nr][nc] == "O":
                    queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        
        return board