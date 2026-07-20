class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, target, final):
            if (not (0 <= r < rows) or
                not (0 <= c < cols) or
                board[r][c] != target):
                return
            
            board[r][c] = final
            dfs(r+1, c, target, final)
            dfs(r-1, c, target, final)
            dfs(r, c+1, target, final)
            dfs(r, c-1, target, final)
            return
        
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and board[r][c] == "O":
                    dfs(r, c, "O", "T")
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    dfs(r, c, "O", "X")
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    dfs(r, c, "T", "O")
        

        
        

                
                
        