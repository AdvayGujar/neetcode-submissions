class Node:
    def __init__(self, val):
        self.val = val
        self.visited = 0
        self.neighbours = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dictionary = {}

        for i in range(numCourses):
            dictionary[i] = Node(i)

        for course, prereq in prerequisites:
            dictionary[prereq].neighbours.append(dictionary[course])

        def dfs(node):
            if dictionary[node].visited == 1:
                return False
            if dictionary[node].visited == 2:
                return True

            dictionary[node].visited = 1

            for neighbour in dictionary[node].neighbours:
                if not dfs(neighbour.val):
                    return False

            dictionary[node].visited = 2

            return True

        for i in range(numCourses):
            if dictionary[i].visited == 0:
                if not dfs(i):
                    return False

        return True