class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            createSubset(i + 1)

        createSubset(0)
        return result