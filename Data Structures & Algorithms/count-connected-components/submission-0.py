class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)
                
            return

        components = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components
