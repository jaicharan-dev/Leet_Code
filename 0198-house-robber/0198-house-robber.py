class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i == 0: return nums[i]
            if i == 1: return max(nums[i], nums[i-1])

            memo[i] = max(dfs(i-2) + nums[i], dfs(i-1))

            return memo[i]

        return dfs(len(nums)-1) 
