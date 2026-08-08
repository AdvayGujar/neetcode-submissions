class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        setOfNums = set()

        for x in range(len(nums)):
            if nums[x] in setOfNums:
                return nums[x]
            else:
                setOfNums.add(nums[x])