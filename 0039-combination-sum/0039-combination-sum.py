class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur_set = []

        def dfs(i, total):
            if total == target:
                res.append(cur_set.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur_set.append(candidates[i])
            dfs(i, total + candidates[i])
            cur_set.pop()
            dfs(i+1, total)
        
        dfs(0, 0)
        return res
