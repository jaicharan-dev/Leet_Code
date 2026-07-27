class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      memo = {} 

      def dfs(i):
        if i in memo: 
          return memo[i]
        if i == 0 or i == 1:
          return 0
        memo[i] = min(cost[i-1] + dfs(i-1), cost[i-2] + dfs(i-2))
        return memo[i]

      return dfs(len(cost))
