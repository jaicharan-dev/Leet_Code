class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_set = []
        used = [False] * len(nums)

        def dfs():
            if len(cur_set) == len(nums):
                res.append(cur_set.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                cur_set.append(nums[i])
                used[i] = True
                dfs()

                cur_set.pop()
                used[i] = False
                        
        dfs()
        return res