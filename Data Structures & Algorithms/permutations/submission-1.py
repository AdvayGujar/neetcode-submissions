class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        
        result = []

        for _ in range(len(nums)):
            first = nums.pop(0)

            permutations = self.permute(nums)

            for p in permutations:
                p.append(first)
            
            result.extend(permutations)
            nums.append(first)
        
        return result