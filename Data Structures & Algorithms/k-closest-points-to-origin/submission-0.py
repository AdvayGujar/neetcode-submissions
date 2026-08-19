class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)

            heapq.heappush_max(heap,[distance, [x,y]])
            if len(heap) > k:
                heapq.heappop_max(heap)

        return list(x[1] for x in heap)