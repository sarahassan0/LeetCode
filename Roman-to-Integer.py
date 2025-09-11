class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            "I" : 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        val = 0

        for i in range(len(s)-1, -1, -1):
            if i < len(s)-1 and roman[s[i]] < roman[s[i+1]]:
                val -= roman[s[i]]
            else:
                val += roman[s[i]]
        return val


#--------------------------O(n) time, O()n space ---------------------------------


        # roman_dict = {
        #     'I': 1,
        #     'V': 5,
        #     'X': 10,
        #     'L': 50,
        #     'C': 100,
        #     'D': 500,
        #     'M': 1000
        # }
        # vals = [roman_dict[x] for x in s]

        # result = 0
        # for i in range(len(vals)):
        #     result += vals[i]
        #     if vals[i] > vals[i-1] and i != 0:
        #         result -= (vals[i-1] * 2)
        # return result

        