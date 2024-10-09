class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i in range(len(s)):
            result = s[i] not in s[0:i] and s[i] not in s[i+1:] 
            if result:
                return i

        return -1
                
        