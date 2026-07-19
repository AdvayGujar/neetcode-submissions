class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        past = set()

        for num in nums:
            if num in past:
                return True
            else:
                past.add(num)
        
        return False