class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_count = {}
        for char in tasks:
            freq_count[char] = 1 + freq_count.get(char, 0)
        
        max_heap = [-freq for char, freq in freq_count.items()]
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
                    cooldown = time + n
                    q.append((freq, cooldown))
            time += 1
        return time

        