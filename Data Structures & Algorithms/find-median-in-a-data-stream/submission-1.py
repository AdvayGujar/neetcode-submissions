class MedianFinder:

    def __init__(self):
        self.firstHeap = []
        self.lastHeap = []

    def addNum(self, num: int) -> None:
        lenFirst = len(self.firstHeap)
        lenLast = len(self.lastHeap)

        if lenFirst == 0 and lenLast == 0:
            heapq.heappush_max(self.firstHeap, num)
        elif num >= self.firstHeap[0]:
            heapq.heappush(self.lastHeap, num)
        else:
            heapq.heappush_max(self.firstHeap, num)

        lenFirst = len(self.firstHeap)
        lenLast = len(self.lastHeap)

        if lenFirst > lenLast + 1:
            heapq.heappush(self.lastHeap, heapq.heappop_max(self.firstHeap))
        elif lenFirst < lenLast:
            heapq.heappush_max(self.firstHeap, heapq.heappop(self.lastHeap))

    def findMedian(self) -> float:
        if len(self.firstHeap) == len(self.lastHeap):
            return (self.firstHeap[0] + self.lastHeap[0]) / 2
        else:
            return self.firstHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()