class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_set = []
        visit = set()

        def dfs():
            if len(cur_set) == len(nums):
                res.append(cur_set.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in visit:
                    continue
                cur_set.append(nums[i])
                visit.add(nums[i])
                dfs()

                cur_set.pop()
                visit.remove(nums[i])
        
        dfs()
        return res