class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj_list = defaultdict(list)
        in_degree = [0] * n

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            in_degree[u] += 1
            in_degree[v] += 1

        leaves = deque()
        for i in range(n):
            if in_degree[i] == 1:
                leaves.append(i)
        
        remaining_nodes = n 
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                
                for neighbor in adj_list[leaf]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 1:
                        leaves.append(neighbor)
                
        return list(leaves)

