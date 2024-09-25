class Solution:
    def reverse(self, x: int) -> int:

        xx = int(str(abs(x))[::-1])
        xx =  -1 * xx if x < 0 else xx
        
        return xx if pow(-2, 31) < xx < pow(2, 31) else 0 