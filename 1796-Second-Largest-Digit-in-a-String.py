class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()

        for c in s:
            if c.isdigit():
                digits.add(int(c))
        
        return sorted(digits, reverse=True)[1] if len(digits) > 1 else -1
        