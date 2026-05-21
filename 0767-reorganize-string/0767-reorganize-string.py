class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for char in s:
            count[char] = 1 + count.get(char, 0)

        maxHeap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = []

        while maxHeap:

            freq, char = heapq.heappop(maxHeap)
            res.append(char)
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None            
            
            freq += 1
            if freq != 0:
                prev = (freq, char)

        return "".join(res) if not prev else ""


