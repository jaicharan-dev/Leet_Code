class Solution:
    def search(self, nums: List[int], target: int) -> int:           
        # find pivot:
        def pivot(nums):
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l] < nums[r]:
                    return l
                mid = (l+r) // 2
                if nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            return r
        # binary search:
        def bs(l,r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        edge = pivot(nums)
        if edge == 0:
            return bs(0, len(nums)-1)
        elif nums[0] <= target:
            return bs(0, edge-1)
        else:
            return bs(edge, len(nums)-1)