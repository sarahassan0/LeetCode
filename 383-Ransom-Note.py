class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        s1 = Counter(ransomNote)
        s2 = Counter(magazine)

        return s1 & s2 == s1
        