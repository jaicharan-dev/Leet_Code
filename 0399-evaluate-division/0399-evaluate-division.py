class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (num, deno), val in zip(equations, values):
            graph[num][deno] = val
            graph[deno][num] = 1.0/val

        def dfs(curr, target, visit):
            if curr not in graph or target not in graph:
                return -1.0
            if curr == target:
                return 1.0
            
            visit.add(curr)
            for neighbor, weight in graph[curr].items():
                if neighbor not in visit:
                    product = dfs(neighbor, target, visit)
                    if product != -1.0:
                        return weight * product
            return -1.0
        
        return [dfs(x, y, set()) for x, y in queries]