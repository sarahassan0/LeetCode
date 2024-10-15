class Solution:
    def minimumSteps(self, s: str) -> int:
        p = 0
        steps = 0

        for i in range(len(s)):
            if s[i] =='0':
                steps += i - p
                p += 1 

        return steps

        