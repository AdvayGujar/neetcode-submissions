class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""

        for char in s:
            if char.isalnum():
                newS += char.lower()

        if newS == "":
            return True
        
        fowardPointer = 0
        reversePointer = len(newS) - 1
        isRunning = True

        while isRunning:

            if newS[fowardPointer] != newS[reversePointer]:
                return False

            if fowardPointer == reversePointer or fowardPointer+1 == reversePointer:
                isRunning = False

            fowardPointer += 1
            reversePointer -= 1

        return True