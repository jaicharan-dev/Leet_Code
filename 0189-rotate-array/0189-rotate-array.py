class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        n = len(nums)
        k = k % n   
        reverse(nums, 0, n-k-1)
        reverse(nums, n-k, n-1)
        reverse(nums, 0, n-1)

        