class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1

        return math.factorial(m + n) // (math.factorial(m) * math.factorial(n))