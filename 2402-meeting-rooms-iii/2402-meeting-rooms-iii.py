class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        freq_map = [0] * n
        available = [i for i in range(n)]
        heapq.heapify(available)
        busy = []

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end,room))
                freq_map[room] += 1
            
            else:
                next_end, room = heapq.heappop(busy)
                duration = end - start
                new_end = next_end + duration
                heapq.heappush(busy, (new_end, room))
                freq_map[room] += 1
        
        max_freq = 0
        res = 0
        for room, freq in enumerate(freq_map):
            if freq > max_freq:
                res = room
                max_freq = freq
        
        return res