class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node      
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._add_node(node)
            return node.val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove_node(self.cache[key])
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_node(new_node)
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove_node(lru_node)
            del self.cache[lru_node.key]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)