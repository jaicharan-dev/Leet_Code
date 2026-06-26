class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [1] * (n+1)

        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                if rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                elif rank[root_v] > rank[root_u]:
                    parent[root_u] = root_v
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1
            
                return True
            return False
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []