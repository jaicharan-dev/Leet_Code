class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur_set = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(cur_set.copy())
                return
            
            if i >= len(candidates) or total > target:
                return 
            
            cur_set.append(candidates[i])
            dfs(i+1, total + candidates[i])

            cur_set.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total)
        
        dfs(0, 0)
        return res