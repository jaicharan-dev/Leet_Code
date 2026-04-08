class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx, num in enumerate(nums):
            compliment = target - num
            if compliment in hashMap:
                return [hashMap[compliment], idx]
            hashMap[num] = idx
        return 