class ListNode:
    
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        val, node = self.map[key]
        self._remove(node)
        self._add(node)
        return val

    def put(self, key: int, value: int) -> None:
        
        if key in self.map:
            _, node = self.map[key]
            self._remove(node)
            self._add(node)
            self.map[key][0] = value
            return
    
        node = ListNode(key)
        self.map[key] = [value, node]
        self._add(node)

        if len(self.map) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]
        
    def _add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)