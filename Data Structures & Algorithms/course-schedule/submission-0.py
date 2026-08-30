class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dictionary = {}

        for i in range(numCourses):
            dictionary[i] = {i}

        for prerequisite in prerequisites:
            if dictionary[prerequisite[0]].intersection(dictionary[prerequisite[1]]):
                return False
            else:
                dictionary[prerequisite[0]].update(dictionary[prerequisite[1]])
        
        return True