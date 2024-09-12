class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        counter = 0
        allowed_set = set(allowed)

        for w in words:
            if set(w).issubset(allowed_set):
                counter += 1
        
        return counter