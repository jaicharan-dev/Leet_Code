class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(street):
            rob1 = 0
            rob2 = 0
            
            for n in street:
                current = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = current
            
            return rob2
        
        street_a_max = helper(nums[:-1])
        street_b_max = helper(nums[1:])

        return max(street_a_max, street_b_max)
        
