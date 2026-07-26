class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for x in range(len(nums)-2):
            if x>0 and nums[x] == nums[x-1]:
                continue
            
            left = x+1
            right = len(nums)-1
            target = 0 - nums[x]
            isRunning = True

            while isRunning:
                if left == right:
                    isRunning = False
                    continue
                if target == nums[left] + nums[right]:
                    result.append([nums[x],nums[left],nums[right]])
                    while nums[left + 1] == nums[left] and left+1 != right:
                        left += 1
                    left += 1 
                elif target > nums[left] + nums[right]:
                    left += 1
                else:
                    right -= 1

        return result

