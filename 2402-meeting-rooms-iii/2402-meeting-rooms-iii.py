class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        room_counts = [0] * n

        available_rooms = [i for i in range(n)]
        heapq.heapify(available_rooms)

        busy_rooms = []

        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room_no = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room_no)

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room))
                room_counts[room] += 1
            
            else:
                nearest_end, room = heapq.heappop(busy_rooms)
                duration = end - start
                new_end = nearest_end + duration
                heapq.heappush(busy_rooms, (new_end, room))
                room_counts[room] += 1
        
        max_meetings = -1
        best_room = -1

        for i in range(len(room_counts)):
            if room_counts[i] > max_meetings:
                max_meetings = room_counts[i]
                best_room = i
        
        return best_room
        