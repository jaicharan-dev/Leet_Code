class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for idx, num in enumerate(nums):
            if num in hash_map and idx - hash_map[num] <= k:
                return True
            else:
                hash_map[num] = idx
                
        return False
