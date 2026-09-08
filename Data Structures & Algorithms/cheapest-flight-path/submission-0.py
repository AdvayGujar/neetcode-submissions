class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for source, destination, price in flights:
            graph[source].append((price, destination))

        minPrice = []
        visited = set()

        def dfs(source, price, stops, minHeap):
            while minHeap:
                p, destination = heapq.heappop(minHeap)

                if destination in visited:
                    return

                visited.add(destination)
                price += p

                if destination == dst:
                    heapq.heappush(minPrice, price)
                elif stops < k:
                    newMinHeap = []
                    for i in range(len(graph[destination])):
                        heapq.heappush(newMinHeap, graph[destination][i])
                    
                    dfs(destination, price, stops + 1, newMinHeap)
                
                price -= p
        
        minHeap = []
        for i in range(len(graph[src])):
            heapq.heappush(minHeap, graph[src][i])
        
        dfs(src, 0, 0, minHeap)
        
        if minPrice:
            return heapq.heappop(minPrice)
        else:
            return -1