class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        intervals.sort(key=lambda x: x[1])
        end_time = intervals[0][1]
        removed_count = 0

        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]


            if curr_start < end_time:
                removed_count += 1
            else:
                end_time = curr_end
        
        return removed_count