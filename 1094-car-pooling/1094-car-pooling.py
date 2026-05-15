class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        minHeap = []
        curr_passengers = 0

        for num_passengers, start, end in trips:

            while minHeap and minHeap[0][0] <= start:
                _, drop_passengers = heapq.heappop(minHeap)
                curr_passengers -= drop_passengers

            curr_passengers += num_passengers

            if curr_passengers > capacity:
                return False

            heapq.heappush(minHeap, (end, num_passengers))

        return True  
