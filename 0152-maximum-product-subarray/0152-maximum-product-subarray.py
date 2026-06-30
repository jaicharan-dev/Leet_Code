class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            choice_a = curr_max * nums[i]
            choice_b = curr_min * nums[i]
            choice_c = nums[i]

            curr_max = max(choice_a, choice_b, choice_c)
            curr_min = min(choice_a, choice_b, choice_c)

            global_max = max(global_max, curr_max)
        
        return global_max