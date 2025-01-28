class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(set(s)) != len(set((t))):
            return False

        charHash = {} 
        for i in range(len(s)):
            char = s[i]
            if char in charHash and  charHash[char] != t[i]:
                return False
            charHash[char] = t[i]
     
        return True