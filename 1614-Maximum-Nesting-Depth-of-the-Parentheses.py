class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        max_depth = 0

        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack[-1] == "(":
                    max_depth = max(max_depth, len(stack))
                    stack.pop()
                else:
                    stack.append(c)

        return max_depth
