class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        counter = {}

        for character in s:
            if character in counter:
                counter[character] += 1
            else:
                counter[character] = 1

        for character in t:
            if character in counter:
                if counter[character] > 0:
                    counter[character] -= 1
                else:
                    return False
            else:
                return False

        return True