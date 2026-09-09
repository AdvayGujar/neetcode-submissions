class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        prev1 = 2
        prev2 = 1
        curr = 0

        for i in range(3, n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return curr