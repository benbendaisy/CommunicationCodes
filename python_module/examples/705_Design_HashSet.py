class MyHashSet:

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