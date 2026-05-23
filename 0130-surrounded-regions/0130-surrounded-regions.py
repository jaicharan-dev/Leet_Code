class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r,c,initial_char,final_char):
            if not (0 <= r < rows) or not (0 <= c < cols) or board[r][c] != initial_char:
                return
            
            board[r][c] = final_char
            dfs(r+1,c,initial_char,final_char)
            dfs(r-1,c,initial_char,final_char)
            dfs(r,c+1,initial_char,final_char)
            dfs(r,c-1,initial_char,final_char)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0,"O","T")
            if board[r][cols-1] == "O":
                dfs(r,cols-1,"O","T")
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c,"O","T")
            if board[rows-1][c] == "O":
                dfs(rows-1,c,"O","T")
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        