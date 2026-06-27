class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        prereq_set = defaultdict(set)
        q = deque()

        for prereq, crs in prerequisites:
            adj_list[prereq].append(crs)
            in_degree[crs] += 1
            prereq_set[crs].add(prereq)
        
        for crs, prereq in enumerate(in_degree):
            if prereq == 0:
                q.append(crs)
        
        while q:
            crs = q.popleft()
            for next_crs in adj_list[crs]:
                prereq_set[next_crs].update(prereq_set[crs])
                in_degree[next_crs] -= 1

                if in_degree[next_crs] == 0:
                    q.append(next_crs)

        res = []

        for u, v in queries:
            res.append(u in prereq_set[v])
        return res 



