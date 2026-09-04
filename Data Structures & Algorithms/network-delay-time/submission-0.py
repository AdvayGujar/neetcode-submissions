import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        minHeap = [(0, k)]
        
        minTime = {}

        while minHeap:
            travelTime, node = heapq.heappop(minHeap)

            if node in minTime:
                continue

            minTime[node] = travelTime

            for neighbor, weight in graph[node]:
                if neighbor not in minTime:
                    heapq.heappush(minHeap, (travelTime + weight, neighbor))

        if len(minTime) < n:
            return -1

        return max(minTime.values())