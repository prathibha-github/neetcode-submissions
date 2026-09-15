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
                if not stack or match[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack
                     