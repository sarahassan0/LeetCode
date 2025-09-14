class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i, j = 0, 0

        while i < len(s):
            while j < len(t):
                if s[i] == t[j]:
                    i += 1;  j += 1
                    break
                else:
                    j += 1

            if i < len(s) and j == len(t):
                return False
        return True 

#---------------------------------------------

        # result = ""
        # for i in s:
        #     for j in range(len(t)):                 
        #         if i == t[j]:
        #             result += i
        #             t= t[j+1:]
        #             break
        # return s == result