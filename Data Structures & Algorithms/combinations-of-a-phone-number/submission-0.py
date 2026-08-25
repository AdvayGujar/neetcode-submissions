class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        def combination(word, digits, index):
            digit = digits[index]

            match digit:
                case '2':
                    letters = ('a', 'b', 'c')

                    for letter in letters:
                        word += letter

                        if len(word) == len(digits):
                            result.append(word)
                        else:
                            combination(word, digits, index + 1)

                        word = word.removesuffix(letter)
                case '3':
                    letters = ('d', 'e', 'f')

                    for letter in letters:
                        word += letter

                        if len(word) == len(digits):
                            result.append(word)
                        else:
                            combination(word, digits, index + 1)

                        word = word.removesuffix(letter)
                case '4':
                    letters = ('g', 'h', 'i')

                    for letter in letters:
                        word += letter

                        if len(word) == len(digits):
                            result.append(word)
                        else:
                            combination(word, digits, index + 1)

                        word = word.removesuffix(letter)
                case '5':
                    letters = ('j', 'k', 'l')

                    for letter in letters:
                        word += letter

                        if len(word) == len(digits):
                            result.append(word)
                        else:
                            combination(word, digits, index + 1)

                        word = word.removesuffix(letter)
                case '6':
                    letters = ('m', 'n', 'o')

                    for letter in letters:
                        word += letter

                        if len(word) == len(digits):
                            result.append(word)
                        else:
                            combination(word, digits, index + 1)

                        word = word.removesuffix(letter)
                case '7':
                    letters = ('p', 'q', 'r', 's')

                    for letter in letters:
                        word += letter

                        if len(word) == len(digits):
                            result.append(word)
                        else:
                            combination(word, digits, index + 1)

                        word = word.removesuffix(letter)
                case '8':
                    letters = ('t', 'u', 'v')

                    for letter in letters:
                        word += letter

                        if len(word) == len(digits):
                            result.append(word)
                        else:
                            combination(word, digits, index + 1)

                        word = word.removesuffix(letter)
                case '9':
                    letters = ('w', 'x', 'y', 'z')

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