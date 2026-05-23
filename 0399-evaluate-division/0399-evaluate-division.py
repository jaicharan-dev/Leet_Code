class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)
        for (num, den), val in zip(equations, values):
            graph[num][den] = val
            graph[den][num] = 1.0/val

        def dfs(curr, target, visited):
            if curr == target:
                return 1
            visited.add(curr)

            for neighbor, weight in graph[curr].items():
                if neighbor not in visited:
                    product = dfs(neighbor, target, visited)
                    if product != -1:
                        return weight * product
            return -1

        results = []
        for X, Y in queries:
            if X not in graph or Y not in graph:
                results.append(-1.0)
            elif X == Y:
                results.append(1.0)
            else:
                results.append(dfs(X, Y, set()))
        
        return results
