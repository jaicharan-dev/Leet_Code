class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        cur_max = nums[0]
        cur_min = nums[0]

        for n in nums[1:]:

            choice_a = n
            choice_b = n * cur_max
            choice_c = n * cur_min

            temp_max = max(choice_a, choice_b, choice_c) 
            cur_min = min(choice_a, choice_b, choice_c)
            cur_max = temp_max

            res = max(res, cur_max)
        
        return res