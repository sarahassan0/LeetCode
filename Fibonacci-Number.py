class Solution:
    def fib(self, n: int) -> int:

################### Iterative - O(n) ##################

        arr = [0, 1]

        for i in range(2, n+1):
            arr.append(arr[i-1] + arr[i-2])

        return arr[n]

################### Recursion - O(2^n) ##################

    #    if n == 0: return 0
    #    if n <= 2: return 1
    #    return self.fib(n-1) + self.fib(n-2)

        
        
        