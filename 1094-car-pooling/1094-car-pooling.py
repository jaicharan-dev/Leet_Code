class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        min_heap = []
        curr_cap = 0
        for people, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                _, people_leaving = heapq.heappop(min_heap)
                curr_cap -= people_leaving

            curr_cap += people
            if curr_cap > capacity:
                return False 
            
            heapq.heappush(min_heap, (end, people))
        
        return True
