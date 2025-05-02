class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = []

        for i in range(rowIndex + 1):
            sub = [1] * (1 + i)
            for j in range(1, i):
                sub[j] = arr[i-1][j-1] + arr[i-1][j]
            arr.append(sub) 

        return arr[-1]
        