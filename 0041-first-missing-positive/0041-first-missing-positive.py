class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums):
                if nums[i] == i+1:
                    i += 1
                else:
                    idx = nums[i]-1 
                    nums[i], nums[idx] = nums[idx], nums[i]
                    if nums[i] == nums[idx]:
                        i += 1
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
        
            