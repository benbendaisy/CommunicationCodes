class MyHashSet1:

    def __init__(self):
        self.myMap = {}

    def add(self, key: int) -> None:
        self.myMap[key] = None
        return None

    def remove(self, key: int) -> None:
        if key in self.myMap:
            self.myMap.pop(key)
        return None

    def contains(self, key: int) -> bool:
        return key in self.myMap

class MyHashSet:
    def __init__(self):
        self.hash_map = {}
        
    def add(self, key: int) -> None:
        self.hash_map[key] = None

    def remove(self, key: int) -> None:
        if key in self.hash_map:
            del self.hash_map[key]

    def contains(self, key: int) -> bool:
        return key in self.hash_map