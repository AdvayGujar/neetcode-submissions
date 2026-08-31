class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        state = [0] * numCourses
        result = []

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True

            state[node] = 1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2
            result.append(node)

            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return []

        return result[::-1]