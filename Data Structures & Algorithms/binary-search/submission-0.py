class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while True:
            mid = int((right + left)/2)
            if nums[mid] == target:
                return mid
            elif nums[right] == target:
                return right
            elif nums[left] == target:
                return left
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid

            if left == right or left == right-1:
                return -1