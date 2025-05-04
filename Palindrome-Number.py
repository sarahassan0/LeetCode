class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
        # to include nigative intgers and int with a single digig
            return False

        reversed_half= 0
        while x > reversed_half:
            digit = x % 10
            reversed_half = (reversed_half * 10) + digit
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10

#--------------------------------------------------------
        # x = str(x)
        # l, r = 0 , len(x) - 1
        
        # while l <= r:

        #     if x[l] == x[r]:
        #         l += 1
        #         r -= 1
        #     else:
        #         return False
        # return True

#-------------------------------------------
        # return str(x) == str(x)[::-1]
        