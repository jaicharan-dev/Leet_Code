class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.capacity = k
        for num in nums:
            if len(self.min_heap) < k:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappushpop(self.min_heap, num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.capacity:
            heapq.heappush(self.min_heap, val)
        else:
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)