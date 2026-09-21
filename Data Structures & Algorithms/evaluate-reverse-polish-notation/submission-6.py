class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for token in tokens:
            if len(stack) >= 2 and token in ("+", "-", "/", "*"):
                num1 = stack.pop()
                num2 = stack.pop()
                #print(num1, " ", num2)
                if token == "+":
                    stack.append(num1+num2)
                elif token == "-":
                    stack.append(num2 - num1)
                elif token == "/":
                    stack.append(int(num2/num1))
                elif token == "*":
                    stack.append(num1*num2)
            else:
                #print(token)
                stack.append(int(token))
        return stack and int(stack[-1])