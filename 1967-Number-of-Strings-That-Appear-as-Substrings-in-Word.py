class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        n = 0

        for s in patterns:
            if s in word:
                n += 1

        return n
        