class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()

        def createSubset(i):
            if i == len(nums):
                result.append(subset[:])
                return
            
            subset.append(nums[i])
            createSubset(i+1)
            subset.pop()

            createSubset(i + 1)

        createSubset(0)
        return result