class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1

        queue = deque()
        for course, freq in enumerate(in_degree):
            if freq == 0:
                queue.append(course)
        res = []
        while queue:
            curr_course = queue.popleft()
            res.append(curr_course)

            for next_course in adj_list[curr_course]:
                in_degree[next_course] -= 1

                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return res if len(res) == numCourses else []