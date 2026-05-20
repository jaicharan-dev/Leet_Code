class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        prereq_sets = [set() for _ in range(numCourses)]

        for prereq, course in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
            prereq_sets[course].add(prereq)
        
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            curr_course = queue.popleft()

            for next_course in adj_list[curr_course]:
                prereq_sets[next_course].update(prereq_sets[curr_course])
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        res = []
        for u,v in queries:
            res.append(u in prereq_sets[v])
        return res