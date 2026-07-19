class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        answer = [0]*n

        for x in range(0,n):
            answer[x] = prefix
            prefix *= nums[x]

        print(answer)

        for x in range(n-1,-1,-1):
            answer[x] *= suffix
            suffix *= nums[x]
            
        return answer