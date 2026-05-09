class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k1 = k % n 
        left = nums[n-k1:]
        right = nums[:n-k1]

        nums1 = left + right
        for i in range(len(nums)):
            nums[i] = nums1[i]
        return nums