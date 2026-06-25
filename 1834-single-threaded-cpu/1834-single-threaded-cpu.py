class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sort_tasks = [(start, process, idx) for idx, (start, process) in enumerate(tasks)]
        sort_tasks.sort()

        curr_time = 0
        i = 0
        min_heap = []
        res = []
        
        while i < len(sort_tasks) or min_heap:
            if not min_heap and curr_time < sort_tasks[i][0]:
                curr_time = sort_tasks[i][0]

            while i < len(sort_tasks) and curr_time >= sort_tasks[i][0]:
                start, process, idx = sort_tasks[i]
                heapq.heappush(min_heap, (process, idx))
                i += 1
            
            process, idx = heapq.heappop(min_heap)
            curr_time += process
            res.append(idx)

        return res

