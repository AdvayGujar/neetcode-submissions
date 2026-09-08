class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for source, destination, price in flights:
            graph[source].append((price, destination))

        minPrice = []
        visited = set()

        def dfs(source, current_price, stops):
            if source == dst:
                heapq.heappush(minPrice, current_price)
                return

            if stops > k:
                return

            visited.add(source)

            for p, destination in graph[source]:
                if destination not in visited:
                    dfs(destination, current_price + p, stops + 1)

            visited.remove(source)

        dfs(src, 0, 0)

        if minPrice:
            return heapq.heappop(minPrice)
        else:
            return -1