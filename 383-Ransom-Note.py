class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(magazine) < len(ransomNote):
            return False

        noteHash, magazineHash = defaultdict(int), defaultdict(int)

        for i in range(len(magazine)):
            magazineHash[magazine[i]] += 1

            if i < len(ransomNote):
                noteHash[ransomNote[i]] += 1
        

        for c in noteHash:
            if noteHash[c] > magazineHash[c]:
                return False

        return True

        