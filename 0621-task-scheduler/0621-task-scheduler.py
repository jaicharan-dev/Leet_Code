class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        self.time = 0
        minHeap = []
        count = Counter(tasks)
        total_tasks = [-val for val in count.values()]
        heapq.heapify(total_tasks)


        while total_tasks or minHeap:
            self.time += 1

            while minHeap and minHeap[0][0] <= self.time:
                _, num_tasks = heapq.heappop(minHeap)
                heapq.heappush(total_tasks, -num_tasks)

            if total_tasks:
                curr_tasks = -heapq.heappop(total_tasks)
                curr_tasks -= 1

                if curr_tasks != 0:
                    heapq.heappush(minHeap, (self.time+n+1, curr_tasks))
        
        return self.time