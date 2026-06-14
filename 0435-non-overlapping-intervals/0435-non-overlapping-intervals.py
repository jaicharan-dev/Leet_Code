class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end_point = intervals[0][1]
        removed = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < end_point:
                removed += 1
            else:
                end_point = end
        return removed