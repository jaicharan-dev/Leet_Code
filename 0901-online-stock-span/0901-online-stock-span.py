class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        span = 1
        i = len(self.arr) - 1
        while self.arr and i >= 0 and price >= self.arr[i][0]:
            span += self.arr[i][1]
            i -= self.arr[i][1]

        self.arr.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)