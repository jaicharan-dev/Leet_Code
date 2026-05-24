class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        queue = deque()
        res = []
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
        
        for course, degrees_needed in enumerate(in_degree):
            if degrees_needed == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            res.append(course)

            for next_course in adj_list[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return res if len(res) == numCourses else []