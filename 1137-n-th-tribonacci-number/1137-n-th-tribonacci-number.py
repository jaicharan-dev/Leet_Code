class Solution:
  def tribonacci(self, n: int) -> int:
    memo = {0:0, 1:1, 2:1}

    def dfs(i):
      if i in memo:
        return memo[i]
      if i == 0: 
        return 1
      
      memo[i] = dfs(i-3) + dfs(i-2) + dfs(i-1)
      return memo[i]
    
    return dfs(n)
