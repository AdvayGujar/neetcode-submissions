class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Direct list lookup instead of hash map + custom Node objects
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 0 = UNVISITED, 1 = VISITING (active path), 2 = VISITED (done)
        state = [0] * numCourses

        def dfs(node: int) -> bool:
            if state[node] == 1:
                return False  # Cycle detected
            if state[node] == 2:
                return True   # Fully verified path

            state[node] = 1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2
            return True

        # Run DFS for all course components
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False

        return True