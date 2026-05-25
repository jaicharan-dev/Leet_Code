class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 
        while l < r:
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                mid = (l+r) // 2
                if nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid
        
        return nums[r]

