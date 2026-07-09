class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        curr_meet = intervals[0]
        res = 0
        i = 1
        while i < len(intervals):
            if curr_meet[1] > intervals[i][0]:
                res += 1
                i += 1
            else:
                curr_meet = intervals[i]
                i += 1

        return res