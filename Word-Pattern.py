class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap = {}
        s = s.split()

        if len(s) != len(pattern): return False 
        
        for i in range(len(s)):
            if pattern[i] in hashMap and hashMap[pattern[i]] != s[i]:
                return False
            elif pattern[i] not in hashMap and s[i] in hashMap.values():
                return False
            hashMap[pattern[i]] = s[i]

        return True
