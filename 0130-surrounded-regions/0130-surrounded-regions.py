class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c, visit):
            if (not (0 <= r < rows) or 
                not (0 <= c < cols)):
                return False
            
            if board[r][c] == "X":
                return True
            
            if board[r][c] == "O" and (r,c) in visit:
                return True 
            
            if board[r][c] == "O" and (r,c) not in visit:
                visit.add((r, c))
                return (dfs(r+1, c, visit) and
                        dfs(r-1, c, visit) and
                        dfs(r, c+1, visit) and
                        dfs(r, c-1, visit))
         
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    visit_set = set()
                    if dfs(r, c, visit_set):
                        for vr, vc in visit_set:
                            board[vr][vc] = "X"
        
                     


