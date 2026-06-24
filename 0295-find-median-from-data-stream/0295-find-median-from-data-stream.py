class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        largest_of_left = -heapq.heappop(self.left)
        heapq.heappush(self.right, largest_of_left)

        if len(self.left) < len(self.right):
            lowest_of_right = heapq.heappop(self.right)
            heapq.heappush(self.left, -lowest_of_right)

    def findMedian(self) -> float:
        
        if len(self.left) > len(self.right):
            return -self.left[0]
        
        return (-self.left[0] + self.right[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()