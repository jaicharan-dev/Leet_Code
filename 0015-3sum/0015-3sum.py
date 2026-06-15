class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            left = i + 1
            right = n - 1
            
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                     
                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1
        return res
