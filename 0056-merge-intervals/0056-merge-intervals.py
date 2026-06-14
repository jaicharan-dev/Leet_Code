class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        res = []
        while i < len(intervals):
            start, end = intervals[i]
            for j in range(i+1, len(intervals)):
                next_start, next_end = intervals[j]
                if end >= next_start:
                    end = max(end, next_end)
                    i = j
                else:
                    break
            res.append([start, end])
            i += 1        
        return res