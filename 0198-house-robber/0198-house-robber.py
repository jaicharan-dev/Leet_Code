class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == -2 or i == -1:
                return 0
            
            memo[i] = max(nums[i] + dfs(i-2), dfs(i-1))
            return memo[i]
        
        return dfs(len(nums)-1)