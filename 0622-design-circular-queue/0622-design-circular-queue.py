class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.length = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        rear = (self.head + self.length) % self.capacity
        self.queue[rear] = value
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        self.length -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        rear = (self.head + self.length - 1) % self.capacity
        return self.queue[rear] 

    def isEmpty(self) -> bool:
        return self.length == 0
            
    def isFull(self) -> bool:
        return self.length == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()