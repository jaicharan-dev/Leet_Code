class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(street):
            rob1 = 0
            rob2 = 0
            for n in street:
                curr = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = curr
            return rob2
                
        street_a = helper(nums[:-1])
        street_b = helper(nums[1:])
        return max(street_a, street_b)