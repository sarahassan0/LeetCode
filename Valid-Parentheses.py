class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        brackets = {
            ')':'(',
            '}':'{',
            ']':'['
            }
        
        stack = []

        for c in s:
            if c in brackets:
                if not stack or brackets[c] != stack.pop():
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
           