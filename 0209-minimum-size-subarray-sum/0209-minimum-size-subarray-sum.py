class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left = 0
        curr_sum = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]

            if curr_sum >= target:
                while curr_sum - nums[left] >= target:
                    curr_sum -= nums[left]
                    left += 1
                
                min_length = min(min_length, right-left+1)

        
        return min_length if min_length != float('inf') else 0


