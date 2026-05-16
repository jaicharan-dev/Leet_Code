class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = x**2 + y**2
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist,x,y))
            else:
                heapq.heappushpop(maxHeap, (-dist,x,y))
        
        return [[x,y] for dist, x, y in maxHeap]

        