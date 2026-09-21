class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = max(nums)
        cur_max = cur_min = 1 

        for num in nums:
            temp = cur_max * num

            cur_max = max(temp, cur_min * num, num)
            cur_min = min(temp, cur_min * num, num)
        
            max_product = max(max_product, cur_max)
        
        return max_product