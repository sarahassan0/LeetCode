class Solution:
    def partitionString(self, s: str) -> int:
        
        num = 1
        substring = ""

        for i in range(len(s)):

            if s[i] not in substring:
                substring += s[i] 
            else:
                substring = s[i]
                num +=1

        return num