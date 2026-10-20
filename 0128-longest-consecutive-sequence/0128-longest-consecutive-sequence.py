class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hash_set = set(nums)
        res = 0
        for n in hash_set:
            if n-1 not in hash_set:
                i = 1
                while n + i in hash_set:
                    i += 1
                res = max(res, i)
        
        return res
