class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.len = 0
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # the key already exists
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            node.val = value
        else:
            node = ListNode(key, value)
            self.map[key] = node
            
            if self.len == self.capacity:
                lru = self.tail.prev
                del self.map[lru.key]
                self._remove(lru)
            else:
                self.len += 1
        self.map[key] = node  
        self._add(node)
        
    def _add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)