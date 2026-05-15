class Solution:
    def reorganizeString(self, s: str) -> str:
        
        count = Counter(s)
        
        maxHeap = [[-freq, char] for char, freq in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = []

        while maxHeap or prev:

            if prev and not maxHeap:
                return ""
            
            freq, char = heapq.heappop(maxHeap)
            res.append(char)

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            freq += 1
            if freq != 0:
                prev = [freq, char]
            
        
        return "".join(res)

