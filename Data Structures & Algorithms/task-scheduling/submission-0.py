class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dictionary = {}

        for x in tasks:
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1

        maxHeap = []
        for x in dictionary:
            heapq.heappush_max(maxHeap, dictionary[x])

        queue = deque()
        timer = 1

        while maxHeap or queue:
            if maxHeap:
                count = heapq.heappop_max(maxHeap)
                if count > 1:
                    queue.append([count - 1, timer + n + 1])
            
            timer += 1

            if queue:
                if queue[0][1] == timer:
                    count = queue.popleft()
                    heapq.heappush_max(maxHeap, count[0])

        return timer - 1