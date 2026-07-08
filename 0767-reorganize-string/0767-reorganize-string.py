class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = []
        count = Counter(s)
        cooldown = None
        for char, freq in count.items():
            heapq.heappush(max_heap, (-freq,char))

        res = ""
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res += char
            freq += 1
            if cooldown:
                heapq.heappush(max_heap, cooldown)
                cooldown = None
            if freq != 0:
                cooldown = (freq, char)
        
        return res if len(res) == len(s) else ""
            

