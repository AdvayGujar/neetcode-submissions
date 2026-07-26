class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(char)
        
        if not stack:
            return True
        else:
            return False