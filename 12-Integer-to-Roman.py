class Solution:
    def intToRoman(self, num: int) -> str:

        nums_map = {
            1: \I\,
            5: \V\,    4: \IV\,
            10: \X\,   9: \IX\,
            50: \L\,   40: \XL\,
            100: \C\,  90: \XC\,
            500: \D\,  400: \CD\,
            1000: \M\, 900: \CM\,
        }

        roman = \\

        for n in sorted(nums_map.keys(), reverse=True):

            if (num // n) >= 1 :
                roman += nums_map[n] * (num // n)
                num -= (num // n) * n

        return roman