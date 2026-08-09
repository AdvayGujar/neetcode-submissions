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
            keys = list(self.dictionary.keys())
            if len(keys) < self.capacity:
                self.dictionary[key] = value
            else:
                self.dictionary.pop(keys[0])
                self.dictionary[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)