class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        occurs = [0] * 26

        for c in s:
            occurs[ord(c) - ord('a')] += 1

        occ = occurs[ord(s[0]) - ord('a')]
        for n in occurs:
            if n != occ and n != 0 :
                return False

        return True
        