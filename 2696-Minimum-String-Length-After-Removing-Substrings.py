class Solution:
    def minLength(self, s: str) -> int:

        stack = []

        for c in s:
            stack.append(c)

            if len(stack) >= 2:
                if stack[-2:] == ['A', 'B'] or stack[-2:] == ['C', 'D']:
                    stack.pop()
                    stack.pop()
        
        return len(stack)

        