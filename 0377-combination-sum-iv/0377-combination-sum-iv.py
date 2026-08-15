class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)

        for t in range(1, target+1):
            for n in nums:
                if t-n == 0:
                    dp[t] += 1
                elif t-n > 0:
                    dp[t] += dp[t-n]
        
        return dp[target]