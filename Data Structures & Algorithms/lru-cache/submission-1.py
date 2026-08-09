class LRUCache:

    def __init__(self, capacity: int):
        self.dictionary = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dictionary:
            value = self.dictionary.pop(key)
            self.dictionary[key] = value
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.dictionary.pop(key)
            self.dictionary[key] = value
        else:
            if len(self.dictionary) < self.capacity:
                self.dictionary[key] = value
            else:
                firstKey = next(iter(self.dictionary))
                self.dictionary.pop(firstKey)
                self.dictionary[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)