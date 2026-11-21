class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                stars.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        while stack and stars:
            left = stack[-1]
            star = stars[-1]
            if star > left:
                stack.pop()
                stars.pop()
            else:
                break
        #print(stack, " ", stars)
        return not stack