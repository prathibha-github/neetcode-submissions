class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if stack and ((c == ')' and stack[-1] == '(') or (c == '}' and stack[-1] == '{') or (c == ']' and stack[-1] == '[')):
                    stack.pop()
                else:
                    return False
        return not stack
                     