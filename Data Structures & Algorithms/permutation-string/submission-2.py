class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lengths1, lengths2 = len(s1), len(s2)

        if lengths1 > lengths2:
            return False

        s1Count = [0]*26
        s2Count = [0]*26

        for x in range(lengths1):
            s1Count[ord(s1[x])-ord('a')] += 1
            s2Count[ord(s2[x])-ord('a')] += 1
            
        matches = sum(1 for i in range(26) if s1Count[i] == s2Count[i])

        for i in range(lengths1, lengths2):
            if matches == 26:
                return True

            inbound = ord(s2[i]) - ord('a')
            s2Count[inbound] += 1
            if s1Count[inbound] == s2Count[inbound]:
                matches += 1
            elif s1Count[inbound] + 1 == s2Count[inbound]:
                matches -= 1 
            
            outbound = ord(s2[i - lengths1]) - ord('a')
            s2Count[outbound] -= 1
            if s1Count[outbound] == s2Count[outbound]:
                matches += 1
            elif s1Count[outbound] - 1 == s2Count[outbound]:
                matches -= 1

        return matches == 26