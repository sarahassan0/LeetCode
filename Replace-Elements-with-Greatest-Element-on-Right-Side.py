class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n = len(arr) 
        maxi = -1

        for i in range(n-1,-1,-1):
                arr[i], tmp = maxi, arr[i]
                if tmp > maxi:
                    maxi = tmp
        return arr

#------------------- will give time limit eventually -----

        # n = len(arr) 
        # for i in range(n-1):
        #     arr[i] = max(arr[i+1:])

        # arr[n-1] = -1
        # return arr