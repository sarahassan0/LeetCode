class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        pattern = {}

        for i in range(len(s)):
            
            if s[i] in pattern and pattern[s[i]] != t[i] :
                return False
            if s[i] not in pattern and t[i] in pattern.values():
                return False

            pattern[s[i]] = t[i]

        return True

        