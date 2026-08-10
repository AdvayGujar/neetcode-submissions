class Node:

    def __init__(self,key = 0, value = 0,next = None, previous = None):
        self.key = key
        self.value = value
        self.next = next
        self.previous = previous

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}

        self.oldest = Node()
        self.latest = Node()
        self.oldest.next = self.latest
        self.latest.previous = self.oldest
        
    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(self.dict[key])
            self.insert(self.dict[key])
            return self.dict[key].value
        else:
            return -1

        
    def remove(self, node):
        previous, next = node.previous, node.next
        previous.next = next
        next.previous = previous

    def insert(self, node):
        node.previous = self.latest.previous
        node.next = self.latest

        self.latest.previous.next = node
        self.latest.previous = node

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        
        self.dict[key] = Node(key, value)
        self.insert(self.dict[key])

        if len(self.dict) > self.capacity:
            oldest = self.oldest.next
            self.remove(oldest)
            self.dict.pop(oldest.key)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)