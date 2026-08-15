class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_global = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for num in nums[1:]:
            option_a = curr_max * num
            option_b = curr_min * num
            option_c = num

            curr_max = max(option_a, option_b, option_c)
            curr_min = min(option_a, option_b, option_c)

            max_global  = max(max_global, curr_max)
        
        return max_global