class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (not (0 <= r < ROWS) or 
                not (0 <= c < COLS) or 
                word[i] != board[r][c]):
               return False
            
            temp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))
            
            board[r][c] = temp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
