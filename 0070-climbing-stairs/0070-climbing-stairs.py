class Solution:
  def climbStairs(self, n: int) -> int:

    memo = [0] * (n+1)

    def dfs(i):
      if i == 0 or i == 1:
        return 1

      if memo[i] != 0:
        return memo[i]
      
      memo[i] = max(memo[i], dfs(i-1) + dfs(i-2))

      return memo[i]
    
    return dfs(n)
