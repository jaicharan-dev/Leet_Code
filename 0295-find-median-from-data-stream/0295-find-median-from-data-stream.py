class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
 
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        
        left_max = -heapq.heappop(self.left)
        heapq.heappush(self.right, left_max)

        if len(self.right) > len(self.left):
            right_min = heapq.heappop(self.right)
            heapq.heappush(self.left, -right_min)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        else:
            return (-self.left[0] + self.right[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()