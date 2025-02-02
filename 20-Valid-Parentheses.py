class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        brackets = {
            '(':')',
            '{':'}',
            '[':']'
            }

        
        stack = []

        for i in s:
            if i in brackets:
                stack.append(brackets[i])
            elif len(stack) == 0 or i != stack.pop():
                return False

        return len(stack) == 0 
        