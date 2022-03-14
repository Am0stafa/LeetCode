class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOPen={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for letter in s:
            if letter in closeToOPen:
                if stack and stack[-1] == closeToOPen[letter]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)
                
        return False if stack else True
        