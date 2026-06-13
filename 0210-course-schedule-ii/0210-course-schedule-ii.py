class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hash_map = defaultdict(list)
        in_degree = [0] * numCourses
        res = []
        for crs, pre in prerequisites:
            hash_map[pre].append(crs)
            in_degree[crs] += 1
        
        queue = deque()
        for idx, freq in enumerate(in_degree):
            if freq == 0:
                queue.append(idx)
        
        while queue:
            crs_completed = queue.popleft()
            res.append(crs_completed)

            for crs in hash_map[crs_completed]:
                in_degree[crs] -= 1
                if in_degree[crs] == 0:
                    queue.append(crs)

        return res if max(in_degree) == 0 else []
                
