class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_of_nums = sum(nums)

        if sum_of_nums % 2 == 1:
            return False
        
        target = sum_of_nums // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for i in range(len(dp) - 1, n - 1, -1):
                if dp[i]:
                    continue
                if dp[i-n]:
                    dp[i] = True
                if dp[-1]:
                    return True
        
        return False