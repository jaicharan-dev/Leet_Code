class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        in_degree = [0] * numCourses
        for crs, pre in prerequisites:
            prereq[pre].append(crs)
            in_degree[crs] += 1
        
        queue = deque()
        for idx, count in enumerate(in_degree):
            if count == 0:
                queue.append(idx)
        
        while queue:
            crs_completed = queue.popleft()
            for crs in prereq[crs_completed]:
                in_degree[crs] -= 1
                if in_degree[crs] == 0:
                    queue.append(crs)

        return True if max(in_degree) == 0 else False 