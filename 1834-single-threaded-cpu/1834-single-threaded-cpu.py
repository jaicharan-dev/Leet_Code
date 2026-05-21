class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_order = [(queue_time, process_time, idx) for idx, (queue_time, process_time) in enumerate(tasks)]
        task_order.sort(key=lambda x: x[0])

        time = 0
        i = 0
        n = len(tasks)
        minHeap = []
        res = []

        while i < n or minHeap:  # processing one element at a time

            if not minHeap and time < task_order[i][0]:
                time = task_order[i][0]

            while i < n and task_order[i][0] <= time:
                _, process_time, idx = task_order[i]
                heapq.heappush(minHeap, (process_time, idx))
                i += 1

            
            process_time, idx = heapq.heappop(minHeap)
            time += process_time
            res.append(idx)
        return res