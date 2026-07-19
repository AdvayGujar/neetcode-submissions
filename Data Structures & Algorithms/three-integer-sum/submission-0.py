class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for x in range(len(nums)-2):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            fP = x+1
            rP = len(nums)-1
            target = 0 - nums[x]
            isRunning = True

            while isRunning:
                if fP == rP:
                    isRunning = False
                    continue
                add = nums[fP] + nums[rP]
                if add == target:
                    result.append([nums[x],nums[fP],nums[rP]])
                    while nums[fP + 1] == nums[fP] and fP+1 != rP:
                        fP += 1
                    fP += 1
                elif add > target:
                    rP -= 1
                else:
                    fP += 1
                
        return result