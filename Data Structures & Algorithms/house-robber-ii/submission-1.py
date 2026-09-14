class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prevVal, maxVal = 0, 0

        for curVal in nums[0:len(nums)-1]:
            temp = max(maxVal, prevVal + curVal)
            prevVal = maxVal
            maxVal = temp
        
        prevValRev, maxValRev = 0, 0

        for curVal in reversed(nums[1:]):
            temp = max(maxValRev, prevValRev + curVal)
            prevValRev = maxValRev
            maxValRev = temp

        return max(maxVal, maxValRev)