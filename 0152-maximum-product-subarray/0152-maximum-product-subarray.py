class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums)):

            choice_a = nums[i]
            choice_b = nums[i] * cur_max
            choice_c = nums[i] * cur_min

            cur_max = max(choice_a, choice_b, choice_c) 
            cur_min = min(choice_a, choice_b, choice_c)
        
            res = max(res, cur_max)
        
        return res