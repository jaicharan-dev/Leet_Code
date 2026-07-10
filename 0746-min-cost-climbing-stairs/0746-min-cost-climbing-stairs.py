class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == 0 or i == 1:
                return 0
            
            one_back = dfs(i-1) + cost[i-1]
            two_back = dfs(i-2) + cost[i-2]

            memo[i] = min(one_back, two_back)
        
            return memo[i]
        
        return dfs(len(cost))