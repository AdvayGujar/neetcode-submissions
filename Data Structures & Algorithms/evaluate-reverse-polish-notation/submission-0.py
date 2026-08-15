class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for x in range(len(tokens)):
            if tokens[x].lstrip("+-").isnumeric():
                stack.append(int(tokens[x]))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if tokens[x] == '*':
                    stack.append(operand1 * operand2)
                elif tokens[x] == '/':
                    stack.append(int(operand1 / operand2))
                elif tokens[x] == '+':
                    stack.append(operand1 + operand2)
                elif tokens[x] == '-':
                    stack.append(operand1 - operand2)
        
        return stack.pop()