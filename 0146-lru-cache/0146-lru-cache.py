class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = ListNode(0, 0)        
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self._remove(node)
        self._add(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._add(node)
            node.val = value
            return
        
        if len(self.map) == self.capacity:
            lru_node = self.tail.prev
            del self.map[lru_node.key]
            self._remove(lru_node)
        
        new_node = ListNode(key, value)
        self._add(new_node)
        self.map[key] = new_node
        
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)