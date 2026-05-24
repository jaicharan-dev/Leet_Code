class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        queue = deque()
        courses_taken = 0
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
        
        for course, freq in enumerate(in_degree):
            if freq == 0:
                queue.append(course)
            
        while queue:
            course = queue.popleft()
            courses_taken += 1

            for next_course in adj_list[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return courses_taken == numCourses

