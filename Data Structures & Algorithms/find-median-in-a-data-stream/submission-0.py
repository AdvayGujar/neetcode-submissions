class MedianFinder:

    def __init__(self):
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)

    def findMedian(self) -> float:
        array = []
        while self.minHeap:
            array.append(heapq.heappop(self.minHeap))

        if len(array) % 2 == 0:
            result = (array[len(array) // 2 - 1] + array[len(array) // 2]) / 2
            heapq.heapify(array)
            self.minHeap = array
            return result
        else:
            result = array[len(array) // 2]
            heapq.heapify(array)
            self.minHeap = array
            return result

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()