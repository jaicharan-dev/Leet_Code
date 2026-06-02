class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path  = []
        candidates.sort()

        def dfs(i, remain):
            if remain == 0:
                res.append(path.copy())
                return
            if i >= len(candidates) or remain < 0:
                return
            
            path.append(candidates[i])
            dfs(i+1, remain - candidates[i])

            path.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1, remain)

        dfs(0, target)
        return res 