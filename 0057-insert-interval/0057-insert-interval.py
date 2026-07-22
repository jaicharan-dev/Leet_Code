class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res = []
        i = 0
        appended = False
        while i < len(intervals):
            interval = intervals[i]

            if interval[1] < start:
                res.append(interval)
            elif interval[0] > end:
                res.append([start, end])
                appended = True
                break
            else:
                start = min(start,interval[0])
                end = max(end, interval[1])

            i += 1
        
        if not appended:
            res.append([start, end])
            return res
        
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res

        