class Solution:
    def checkValidString(self, s: str) -> bool:
        openings = []
        stars = []
        for i in range(len(s)):
            if s[i] == '(':
                openings.append(i)
            elif s[i] == '*':
                stars.append(i)
            elif s[i] == ')':
                if openings:
                    openings.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        while openings and stars:
            left = openings[-1]
            star = stars[-1]
            if star > left:
                openings.pop()
                stars.pop()
            else:
                break
        #print(stack, " ", stars)
        return not openings