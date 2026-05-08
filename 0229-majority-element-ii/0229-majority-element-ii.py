class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashSet = {}

        for num in nums:
            hashSet[num] = 1 + hashSet.get(num, 0)
        
        res = []
        n = len(nums) // 3

        for num, count in hashSet.items():
            if count > n:
                res.append(num)
        
        return res 