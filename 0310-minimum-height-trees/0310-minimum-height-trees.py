class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)
        in_degree = [0] * n

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            in_degree[u] += 1
            in_degree[v] += 1
        
        leaves = deque()
        for i in range(n):
            if in_degree[i] == 1 or in_degree[i] == 0:
                leaves.append(i)
        
        nodes_left = n
        while nodes_left > 2:
            nodes_left -= len(leaves)

            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                for neighbor in adj_list[leaf]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 1:
                        leaves.append(neighbor)
        return list(leaves)

