class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for x in range(0, len(nums)):
            if nums[x] in dictionary:
                dictionary[nums[x]].append(x)
            else:
                dictionary[nums[x]] = []
                dictionary[nums[x]].append(x)
            
            remainder = target - nums[x]

            if remainder == nums[x]:
                if len(dictionary.get(nums[x])) > 1:
                    return dictionary.get(nums[x])
                else:
                    continue

            if remainder in dictionary:
                y = dictionary.get(remainder)
                if y[0] > x:
                    return [x, y[0]]
                else:
                    return [y[0], x]