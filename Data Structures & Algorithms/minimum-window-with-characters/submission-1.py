class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        characterInT = defaultdict(int)

        for character in t:
            if character not in characterInT:
                characterInT[character] = 1
            else:
                characterInT[character] += 1

        targetLength = len(t)
        minWindow = (0, float('inf'))
        startIndex = 0

        for endIndex, ch in enumerate(s):
            if characterInT[ch] > 0:
                targetLength -= 1
            characterInT[ch] -= 1

            if targetLength == 0:
                while True:
                    charAtStart = s[startIndex]
                    if characterInT[charAtStart] == 0:
                        break
                    characterInT[charAtStart] += 1
                    startIndex += 1

                if endIndex - startIndex < minWindow[1] - minWindow[0]:
                    minWindow = (startIndex, endIndex)

                characterInT[s[startIndex]] += 1
                targetLength += 1
                startIndex += 1

        return "" if minWindow[1] > len(s) else s[minWindow[0]:minWindow[1]+1]