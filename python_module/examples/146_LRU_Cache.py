class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        node = self.cache_dict[key]
        self.remove(node)
        self.add(node)
        return node.value
    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            old_node = self.cache_dict[key]
            self.remove(old_node)
        node = ListNode(key, value)
        self.cache_dict[key] = node
        self.add(node)
        if len(self.cache_dict) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.cache_dict[node_to_delete.key]
    def add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
class LRUCache2:
    """
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

    Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    The functions get and put must each run in O(1) average time complexity.

    Example 1:

    Input
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output
    [null, null, null, 1, null, -1, null, -1, 3, 4]

    Explanation
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4
    """
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return self.cache.get(key)
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                del self.cache[next(iter(self.cache))]
        else:
            self.cache.pop(key)
        self.cache[key] = value

class LRUCache:
    def __init__(self, capacity: int):
       self.cache = {}
       self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                self.cache.pop(next(iter(self.cache)))
        else:
            self.cache.pop(key)
        self.cache[key] = value