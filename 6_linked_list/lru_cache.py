# LeetCode Link: https://leetcode.com/problems/lru-cache/


# Solution 1: Generalized Solution - Intended by the interviewer
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.front = Node()
        self.back = Node()
        self.front.next = self.back
        self.back.prev = self.front

    def insert(self, new_node: Node):
        # Insert a new node at the front (MRU) of the linked list.
        prev_node = self.back.prev
        next_node = self.back
        prev_node.next = new_node
        next_node.prev = new_node
        new_node.prev = prev_node
        new_node.next = next_node

    def remove(self, node: Node):
        # Remove a node from the linked list by updating the pointers of adjacent nodes.
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            # If the key is in the cache, it is accessed.
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key is already in the cache, we remove it and update its value.
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # If the cache exceeds its capacity, we remove the least recently used (LRU) item.
            lru = self.front.next
            self.remove(lru)
            self.cache.pop(lru.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)


# Solution 2: Hacky Solution - works only for Python
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the LRUCache with a specified capacity.
        self.capacity = capacity
        self.cache = (
            OrderedDict()
        )  # An OrderedDict for key-value pairs that maintains the order.

    def get(self, key: int) -> int:
        if key in self.cache:
            # If the key is in the cache, it's accessed.
            # To maintain the LRU order, we move the accessed item to the end of the OrderedDict.
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1  # Key not found in the cache.

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key is already in the cache, we move it to the end to represent its recent use.
            self.cache.move_to_end(key)
        self.cache[key] = value  # Add or update the key-value pair in the cache.

        if len(self.cache) > self.capacity:
            # If the cache exceeds its capacity, we need to remove the least recently used (LRU) item.
            # We do this by popping the first item (LRU) from the OrderedDict.
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
