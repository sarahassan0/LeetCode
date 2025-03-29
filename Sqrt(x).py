class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x // 2 + 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if mid ** 2 < x :
                l = mid + 1
            elif  mid ** 2 > x:
                r = mid - 1
            else:
                return mid
        return r



#------------- brute force, O(sqrt(n)) --------
        # if x * x == x:
        #     return x

        # for i in range(x + 1):  
        #     if i * i > x:
        #         return i - 1
                        
           