class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = [(0, 0)]  # (cost, node_index)
        visited = set()
        total_cost = 0

        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)

            # Skip nodes that have already been finalized into the MST
            if u in visited:
                continue

            visited.add(u)
            total_cost += cost

            # Add edges from the newly added node u to all unvisited nodes
            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (dist, v))

        return total_cost