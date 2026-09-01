class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges) + 1)]

        def is_connected(source: int, target: int, visited: set) -> bool:
            if source == target:
                return True
            visited.add(source)
            for neighbor in graph[source]:
                if neighbor not in visited:
                    if is_connected(neighbor, target, visited):
                        return True
            return False

        # Add edges one by one; if both endpoints are already connected, it's redundant
        for u, v in edges:
            if graph[u] and graph[v] and is_connected(u, v, set()):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)

        return []