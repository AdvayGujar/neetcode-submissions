class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            result.append([])
            result.append([nums[0]])
            return result

        nextResult = self.subsets(nums[1:])

        for arr in nextResult:
            result.append(arr)
            result.append([nums[0]] + arr)
        
        return result