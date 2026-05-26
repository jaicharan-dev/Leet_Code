# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 0, n-1
        while l < r:
            mid = (l+r)//2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid + 1
            else:
                r = mid
        peak = l

        l, r = 0, peak
        while l <= r:
            mid = (l+r) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = peak, n-1
        while l <= r:
            mid = (l+r) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
