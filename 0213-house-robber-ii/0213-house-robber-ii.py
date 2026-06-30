class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rob_last = self.helper(nums[1:])
        skip_last = self.helper(nums[:n-1])

        return max(rob_last, skip_last, nums[0])
    
    def helper(self, nums):
        rob1 = 0
        rob2 = 0

        for n in nums:
            rob_this = (n+rob2)
            rob_not = rob1

            rob2 = rob1
            rob1 = max(rob_this, rob_not)

        return rob1
        



