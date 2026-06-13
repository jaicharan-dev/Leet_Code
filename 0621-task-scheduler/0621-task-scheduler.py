class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-freq for freq in count.values()]
        heapq.heapify(max_heap)
        queue = deque()
        time = 0
        while max_heap or queue:
            while queue and time > queue[0][1]:
                task_freq, _ = queue.popleft()
                heapq.heappush(max_heap, task_freq)
            if max_heap:
                freq = heapq.heappop(max_heap)
                freq += 1
                if freq != 0:
                    cooldown_time = time + n
                    queue.append((freq, cooldown_time))
            time += 1
        return time
