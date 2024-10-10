class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        # binary = format(num, 'b')

        comp = \\
        for n in binary:
            comp += '0' if n == '1' else '1'

        return int(comp, 2)

        