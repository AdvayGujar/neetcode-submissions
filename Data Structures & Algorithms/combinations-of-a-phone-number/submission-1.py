class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        keypad = {'2': ('a', 'b', 'c'),
                  '3': ('d', 'e', 'f'),
                  '4': ('g', 'h', 'i'),
                  '5': ('j', 'k', 'l'),
                  '6': ('m', 'n', 'o'),
                  '7': ('p', 'q', 'r', 's'),
                  '8': ('t', 'u', 'v'),
                  '9': ('w', 'x', 'y', 'z')}

        def combination(word, digits, index):
            digit = digits[index]
            letters = keypad[digit]

            for letter in letters:
                word += letter

                if len(word) == len(digits):
                    result.append(word)
                else:
                    combination(word, digits, index + 1)

                word = word.removesuffix(letter)

        if digits == "":
            return result
        else:
            combination("", digits, 0)
        
        return result