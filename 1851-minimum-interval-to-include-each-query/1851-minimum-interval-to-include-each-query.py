class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        sorted_queries = sorted((q,i) for i, q in enumerate(queries))
        
        res = [-1] * len(queries)
        active_intervals = []
        i = 0

        for query, original_idx in sorted_queries:

            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                size = end - start + 1
                heapq.heappush(active_intervals, (size, end))
                i += 1
            
            while active_intervals and active_intervals[0][1] < query:
                heapq.heappop(active_intervals)

            if active_intervals:
                res[original_idx] = active_intervals[0][0]
        
        return res


