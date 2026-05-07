class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashSet = {}
        for num in nums:
            hashSet[num] = 1 + hashSet.get(num, 0) 
        n = len(nums) // 3
        res = []
        for num, freq in hashSet.items():
            if freq > n:
                res.append(num)
        
        return res

        
