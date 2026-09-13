class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return ""

        def isPalindrome(s, left, right):
            counter = 0
            while left >=0 and right < len(s) and s[left] == s[right]:
                counter += 1
                left -= 1
                right += 1
            return counter

        start = 0
        end = 0

        result = 0

        for i in range(len(s)):
            odd = isPalindrome(s, i, i)
            even = isPalindrome(s,i, i+1)

            result += (odd + even)
        
        return result