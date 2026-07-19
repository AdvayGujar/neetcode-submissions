class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for word in strs:
            length = len(word)
            string += str(length)+ "/" + word

        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        result = []
        x = 0
        y = 0
        start = 0

        while x < len(s):
            if s[x+1] == "/":
                y = x
                start = int(s[x])
            else:
                y = x
                while s[y+1] != "/":
                    y += 1
                
                start = int(s[x : y+1])

            print(start)
            # 2. Slice from after the length digit to (current position + 1 + length)
            newString = s[y + 2 : y + 2 + start]
            print(newString)
            result.append(newString)

            # 3. Correctly move the pointer past the digit and the word
            x = y + 2 + start
            print(x)

        return result