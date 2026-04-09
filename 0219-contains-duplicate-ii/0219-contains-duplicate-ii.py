class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_indices = {}

        for i, num in enumerate(nums):
            if num in seen_indices and i - seen_indices[num] <= k:
                return True
            
            seen_indices[num] = i
        
        return False