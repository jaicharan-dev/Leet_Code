class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        max_heap = [-freq for char, freq in count.items()]
        heapq.heapify(max_heap)

        q = deque()
        time = 0

        while max_heap or q:
            while q and time > q[0][1]:
                freq, end_time = q.popleft()
                heapq.heappush(max_heap, freq)

            if max_heap:
                freq = heapq.heappop(max_heap)
                freq += 1
                if freq != 0:
                    cool_down = time + n
                    q.append((freq, cool_down))
            
            time += 1

        return time

