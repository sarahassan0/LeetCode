class Solution:
    def invert(self, s):
        return ''.join('1' if c == '0' else '0' for c in s)

    def findKthBit(self, n: int, k: int) -> str:
        cache = {
            1: "0",
            2: "011",
            3: "0111001",
            4: "011100110110001",
        }

        if n in cache:
            return cache[n][k-1]
        else:
            i = 5
            while i <= n:
                cache[i] = cache[i-1] + "1" + self.invert(cache[i - 1])[::-1]
                i += 1
                
        return cache[n][k-1]
        