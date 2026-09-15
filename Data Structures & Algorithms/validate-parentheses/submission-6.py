class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            "]":"[",
            "}":"{",
            ")":"(",
        }
        for c in s:
            if c in match:
                if stack and match[c] == stack[-1]:
                    stack.pop()
                    continue
            stack.append(c)
        return not stack
                     