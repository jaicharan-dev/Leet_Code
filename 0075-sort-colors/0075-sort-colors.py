class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        r = len(nums)-1
        while l < r:
            if nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        

