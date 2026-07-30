class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] <= nums[right]:
            return nums[left]

        if right == 1:
            return min(nums[left], nums[right])

        firstNum = nums[left]
        lastNum = nums[right]

        while left <= right:
            mid = (right + left) // 2

            if nums[mid-1] > nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif nums[mid-1] < nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            elif firstNum < nums[mid] > lastNum:
                left = mid + 1
            elif firstNum > nums[mid] < lastNum:
                right = mid - 1
                