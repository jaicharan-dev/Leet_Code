class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        for i in range(k+1):
            if i < len(nums):
                hashset.add(nums[i])
        if len(hashset) < min(k+1,len(nums)):
            return True
        
        left = 0
        for right in range(k+1, len(nums)):
            hashset.remove(nums[left])
            left += 1
            hashset.add(nums[right])
            if len(hashset) < k+1:
                return True
        
        return False
    




