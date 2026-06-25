class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for cnt, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                heapq.heappush(max_heap, (cnt, char))
        
        res = []
        
        while max_heap:
            if len(res) >= 2 and res[-1] == res[-2] == max_heap[0][1]:
                freq1, char1 = heapq.heappop(max_heap)

                if not max_heap:
                    break
                
                freq2, char2 = heapq.heappop(max_heap)
                res.append(char2)
                freq2 += 1
                if freq2 != 0:
                    heapq.heappush(max_heap, (freq2, char2))

                heapq.heappush(max_heap, (freq1, char1))
                

            freq, char = heapq.heappop(max_heap)
            res.append(char)
            freq += 1
            if freq != 0:
                heapq.heappush(max_heap, (freq, char))
        
        return "".join(res)