class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        if len(s) == 1:
            if s[0] != '0':
                return 1
        
        if len(s) == 2:
            if int(s) == 10:
                return 1
            if int(s) <= 26:
                return 2
            else:
                return 1
        
        if s[1] == '0':
            curr, prev = 1, 1
        else:
            curr, prev = 2, 1

        for i in range(2, len(s)):
            if s[i] != '0' and (10 <= int(s[i-1] + s[i]) <= 26):
                temp = curr + prev
                prev = curr
                curr = temp
            elif s[i] == '0' and (10 <= int(s[i-1] + s[i]) <= 26):
                temp = prev
                prev = curr
                curr = temp
            elif s[i] != '0' and not (10 <= int(s[i-1] + s[i]) <= 26):
                prev = curr
            else:
                return 0
        
        return curr