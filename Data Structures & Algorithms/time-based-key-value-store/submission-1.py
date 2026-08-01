class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dictionary:
            self.dictionary[key].append([timestamp, value])
        else:
            self.dictionary[key] = []
            self.dictionary[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        tv = self.dictionary.get(key)

        if not tv:
            return ""

        left = 0
        right = len(tv) - 1
        result = ""

        while left <= right:
            mid = (right+left) // 2

            if tv[mid][0] <= timestamp:
                result = tv[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)