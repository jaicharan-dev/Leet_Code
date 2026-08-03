class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        cur_set = set()

        def dfs(i):
            if i == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in cur_set:
                    continue
                path.append(num)
                cur_set.add(num)
                
                dfs(i+1)

                path.pop()
                cur_set.remove(num)
        
        dfs(0)
        return res