class Solution:
    def addDigits(self, num: int) -> int:

        if num < 10 : return num

        num = str(num)
        i, result = 0, 0

        while len(num) > 1:   

            if i == len(num):
                num = str(result)
                i, result = 0, 0

            result += int(num[i])
            i += 1


        return result

        