class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []

        for i in range(numRows):
            sub = [1] * (i + 1) 
            for j in range(1, i):
                sub[j] = arr[i-1][j-1] + arr[i-1][j]
            arr.append(sub)
        return arr
                


        