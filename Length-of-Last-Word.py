class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        l = 0
        for c in s.strip():
            if c == " ":
                l = 0
            else:
                l += 1
                
        return l
#---------------------------------------------

        # return len(s.split()[-1])
        