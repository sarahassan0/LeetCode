class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x // 2 + 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if x > mid ** 2:
                l = mid + 1
            elif x < mid ** 2:
                r = mid - 1
            else:
                return mid
        return r  # since i want the rounded down to the nearest int will retutn r because its  lowering with each loop


#------------- brute force, O(sqrt(n)) --------
        # if x**2 == x:
        #     return x

        # for i in range(x+1):  
        #     if i **2 > x:
        #         return i - 1




                        
           







