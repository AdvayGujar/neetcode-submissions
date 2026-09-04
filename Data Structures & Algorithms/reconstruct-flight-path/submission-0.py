class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for fromAirport, toAirport in tickets:
            heapq.heappush(graph[fromAirport], toAirport)

        result = []
        
        def dfs(airport):
            while graph[airport]:
                nextAirport = heapq.heappop(graph[airport])
                dfs(nextAirport)

            result.append(airport)

        dfs("JFK")

        return result[::-1]