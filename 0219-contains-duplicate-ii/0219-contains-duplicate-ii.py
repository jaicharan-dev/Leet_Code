class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        values = [(idx, num) for idx, num in enumerate(nums)]
        values.sort(key=lambda x: x[1])
        for i in range(1,len(nums)):
            if values[i][1] == values[i-1][1] and values[i][0] - values[i-1][0] <= k:
                return True
        return False
                
