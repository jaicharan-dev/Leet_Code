class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        
        memo = {}

        def dfs(i):
            if i in memo: return memo[i]
            if i == 0: return 0

            min_cnt = float("inf")
            for s in squares:
                if i-s >= 0:
                    curr_cnt = 1 + dfs(i-s)
                    min_cnt = min(min_cnt, curr_cnt)
            
            memo[i] = min_cnt
            return memo[i]
        
        result = dfs(n)
        return result