class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for n in nums:
            freqMap[n] = 1 + freqMap.get(n,0)
        
        heap = []
        for num, freq in freqMap.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]

