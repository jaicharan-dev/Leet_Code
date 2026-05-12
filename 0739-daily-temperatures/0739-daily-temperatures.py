class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):            
            while stack and t > stack[-1][0]:
                _, prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            
            stack.append((t, i))   
        
        return res