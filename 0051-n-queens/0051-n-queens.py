class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        
        cols = set()
        posDiag = set()
        negDiag = set() 

        def dfs(r):
            if r == n:
                formatted_board = ["".join(row) for row in board]
                res.append(formatted_board)
                return
            
            for c in range(n):
                
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                dfs(r + 1)
                
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        dfs(0)
        return res