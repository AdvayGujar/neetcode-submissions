class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def isPalindrome(s, left, right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        end = 0

        for i in range(len(s)):
            odd = isPalindrome(s, i, i)
            even = isPalindrome(s,i, i+1)
            maxLength = max(odd, even)

            if maxLength > end - start:
                start = i - (maxLength - 1) // 2
                end = i + maxLength // 2
        
        return s[start:end + 1]