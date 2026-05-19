class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        queue = deque()

        for r in range(rows):
            if board[r][0] == "O":
                board[r][0] = "T"
                queue.append((r,0))
            if board[r][cols-1] == "O":
                board[r][cols-1] = "T"
                queue.append((r,cols-1))
            
        for c in range(cols):
            if board[0][c] == "O":
                board[0][c] = "T"
                queue.append((0,c))
            if board[rows-1][c] == "O":
                board[rows-1][c] = "T"
                queue.append((rows-1,c))
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0 <= nr < rows) and (0 <= nc < cols) and board[nr][nc] == "O":
                    board[nr][nc] = "T"   
                    queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        