class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {} 

        self.head, self.tail = Node(0, 0), Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prev_mru = self.tail.prev
        
        prev_mru.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev_mru

    def get(self, key: int) -> int:
        if key in self.cache_map:
            accessed_node = self.cache_map[key]
            self.remove(accessed_node)
            self.insert(accessed_node)
            return accessed_node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.remove(self.cache_map[key])
            
        new_node = Node(key, value)
        self.cache_map[key] = new_node
        self.insert(new_node)

        if len(self.cache_map) > self.capacity:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.cache_map[lru_node.key]
