class Solution:
    def reorganizeString(self, s: str) -> str:
        freqMap = {}
        for char in s:
            freqMap[char] = 1 + freqMap.get(char, 0)
        
        minHeap = []
        for char, freq in freqMap.items():
            heapq.heappush(minHeap, (-freq, char))
        
        res = ""
        i = -1
        while minHeap:
            if i != -1 and res[i] != minHeap[0][1]:
                freq, char = heapq.heappop(minHeap)
                res += char
                freq += 1
            
            elif i != -1 and res[i] == minHeap[0][1]:
                if len(minHeap) == 1:
                    return ""
                else:
                    freq1, char1 = heapq.heappop(minHeap)
                    freq, char = heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (freq1, char1))
                    res += char
                    freq += 1

            else:
                freq, char = heapq.heappop(minHeap)
                res += char
                freq += 1
            
            i += 1

            if freq < 0 :
                heapq.heappush(minHeap, (freq, char))
        return res