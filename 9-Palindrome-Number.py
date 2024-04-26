class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = str(x).strip()
        print( arr , arr[::-1] )
        return arr == arr[::-1]  
        