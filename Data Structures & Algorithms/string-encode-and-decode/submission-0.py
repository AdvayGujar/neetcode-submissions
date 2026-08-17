class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for word in strs:
            length = len(word)
            string += str(length) + word

        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        result = []
        x = 0

        while x < len(s):
            # 1. Read the length of the upcoming word
            start = int(s[x]) 

            # 2. Slice from after the length digit to (current position + 1 + length)
            newString = s[x + 1 : x+ 1 + start]
            result.append(newString)

            # 3. Correctly move the pointer past the digit and the word
            x += 1 + start

        return result