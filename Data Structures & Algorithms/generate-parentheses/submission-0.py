class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(res, openBrackets, closeBrackets, maxBrackets):
            if len(res) == maxBrackets * 2:
                result.append(res)
            
            if openBrackets < maxBrackets:
                backtrack(res + "(", openBrackets + 1, closeBrackets, maxBrackets)
            
            if closeBrackets < openBrackets:
                backtrack(res + ")", openBrackets, closeBrackets + 1, maxBrackets)

        backtrack("", 0, 0, n)

        return result