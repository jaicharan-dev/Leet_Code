class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        
        res = [-1] * len(queries)
        sort_queries = sorted([(q,i) for i, q in enumerate(queries)])
        
        i = 0
        min_heap = []

        for query, idx in sort_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]

                heapq.heappush(min_heap, (end-start+1, end))
                i += 1
            
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            if min_heap:
                res[idx] = min_heap[0][0]
        
        return res
