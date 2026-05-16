class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        queue = deque()
        count = Counter(tasks)
        total_tasks = [-val for val in count.values()]
        heapq.heapify(total_tasks)


        while total_tasks or queue:
            time += 1

            if queue and queue[0][0] <= time:
                _, num_tasks = queue.popleft()
                heapq.heappush(total_tasks, -num_tasks)

            if total_tasks:
                curr_tasks = -heapq.heappop(total_tasks)
                curr_tasks -= 1

                if curr_tasks != 0:
                    queue.append((time+n+1, curr_tasks))
        
        return time