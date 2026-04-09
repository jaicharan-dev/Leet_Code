class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        min_subarray = float('inf')
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_subarray = min(min_subarray, right-left+1)
                curr_sum -= nums[left]
                left += 1
        if min_subarray == float('inf'):
            return 0
        return min_subarray