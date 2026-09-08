class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Build the adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        # Array to store the minimum cost to reach each node
        min_cost = [float('inf')] * n
        min_cost[src] = 0

        # Queue stores tuples of (current_node, current_price)
        queue = deque([(src, 0)])
        stops = 0

        # BFS level-by-level up to k + 1 edges (k stops)
        while queue and stops <= k:
            size = len(queue)
            # Create a copy of min_cost for the current level to prevent
            # updating and using costs within the same iteration level
            temp_cost = list(min_cost)

            for _ in range(size):
                curr, cost = queue.popleft()

                for neighbor, price in graph[curr]:
                    if cost + price < temp_cost[neighbor]:
                        temp_cost[neighbor] = cost + price
                        queue.append((neighbor, cost + price))

            min_cost = temp_cost
            stops += 1

        return min_cost[dst] if min_cost[dst] != float('inf') else -1