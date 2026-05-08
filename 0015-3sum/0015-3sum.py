class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue           
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                value = nums[left] + nums[right]
                if value == target:
                    res.append([-target, nums[left], nums[right]])
                    while left < len(nums)-1 and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    while right > 0 and nums[right] == nums[right - 1]:
                        right -= 1 
                    right -= 1
                elif value < target:
                    while left < len(nums)-1 and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                else:
                    while right > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
        return res

