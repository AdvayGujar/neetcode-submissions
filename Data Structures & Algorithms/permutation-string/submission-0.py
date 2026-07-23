class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        characterSet = {}
        left = 0
        right = 0

        for character in s1:
            if character not in characterSet:
                characterSet[character] = 1
            else:
                characterSet[character] += 1

        while right < len(s2):
            if s2[right] in characterSet and characterSet.get(s2[right]) > 0:
                characterSet[s2[right]] -= 1
                if max(characterSet.values()) == 0:
                    return True
                else:
                    right += 1
            elif s2[right] in characterSet:
                while True:
                    characterSet[s2[left]] += 1
                    if s2[left] == s2[right]:
                        left += 1
                        break
                    else:
                        left += 1
            else:
                while left < right:
                    characterSet[s2[left]] += 1
                    left += 1
                left += 1
                right += 1

        return False