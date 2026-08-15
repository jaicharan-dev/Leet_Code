class Solution:
    def rob(self, nums: List[int]) -> int:
        pattern1 = self._max_money(nums[:-1])
        pattern2 = self._max_money(nums[1:])
        pattern3 = nums[0] 
        return max(pattern1, pattern2, pattern3)

    def _max_money(self, arr):
        memo = [float("-inf")] * len(arr)

        def dfs(i):
            if i == -2 or i == -1:
                return 0

            if memo[i] != float("-inf"):
                return memo[i]
            
            memo[i] = max(dfs(i-2) + arr[i], dfs(i-1))
            return memo[i]
        
        return dfs(len(arr)-1)