class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        Tasks = [(queue_time, process_time, i) for i, (queue_time, process_time) in enumerate(tasks)]
        Tasks.sort(key = lambda x: x[0])

        time = 0
        i = 0
        minHeap = []
        res = []
        n = len(tasks)
        
        while i < n or minHeap:

            if not minHeap and time < Tasks[i][0]:
                time = Tasks[i][0]
            
            while i < n and Tasks[i][0] <= time:
                _, process_time, idx = Tasks[i]

                heapq.heappush(minHeap, (process_time, idx))
                i += 1
            
            process_time, idx = heapq.heappop(minHeap)

            time += process_time
            res.append(idx)
        
        return res