class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        return len(s) == len(goal) and s in goal * 2

# -------------- Another detailed soulotion --------

        # if len(s) != len(goal): return False

        # for i in range(len(s)):
        #     if s == goal:
        #         return True

        #     s = s[1:]+s[0]
        
        # return False
        