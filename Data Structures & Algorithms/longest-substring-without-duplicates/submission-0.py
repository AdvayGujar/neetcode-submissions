class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sP = 0
        eP = 0
        longest = 0
        tempLongest = 0

        while eP < len(s):
            if eP == sP:
                tempLongest = 1
                longest = max(tempLongest, longest)
                eP += 1
                continue
            y = 0
            for x in range(sP,eP):
                if s[x] == s[eP]:
                    tempLongest = tempLongest - (y+1)
                    sP = x+1
                    break
                y += 1

            tempLongest += 1
            longest = max(tempLongest, longest)
            eP += 1

        return longest