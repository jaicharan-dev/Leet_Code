class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board), len(board[0])
        global_set = set() 

        def dfs(r, c, cur_set):
            if (not (0 <= r < rows) or not (0 <= c < cols)):
                return True
            
            if board[r][c] == "X" or (r,c) in global_set:
                return False
            
            global_set.add((r, c))
            cur_set.append((r, c))

            up = dfs(r+1, c, cur_set)
            down = dfs(r-1, c, cur_set)
            left = dfs(r, c+1, cur_set)
            right = dfs(r, c-1, cur_set)

            return up or down or left or right
         
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in global_set:
                    cur_set = []
                    if not dfs(r, c, cur_set):
                        for vr, vc in cur_set:
                            board[vr][vc] = "X"
        
                     


