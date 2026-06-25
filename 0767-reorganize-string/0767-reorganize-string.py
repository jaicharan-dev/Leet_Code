class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        prev = None
        res = []
        
        while max_heap:

            freq, char = heapq.heappop(max_heap)
            res.append(char)

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            
            freq += 1
            if freq != 0:
                prev = (freq, char)
            
        return "".join(res) if not prev else ""