class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        heap = []

        for num in dictionary:
            heapq.heappush(heap, (dictionary[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]