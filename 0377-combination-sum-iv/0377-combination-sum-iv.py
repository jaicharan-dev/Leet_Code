class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i):
            if i in memo: return memo[i]
            if i == 0: return 1
            if i < 0: return 0

            total_ways = 0
            for num in nums:
                total_ways += dfs(i-num)

            memo[i] = total_ways
            return memo[i]
        
        return dfs(target)

