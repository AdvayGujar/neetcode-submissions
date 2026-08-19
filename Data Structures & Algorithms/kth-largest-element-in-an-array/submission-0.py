class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for x in nums:
            heapq.heappush(minHeap, x)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]