class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for r in zero_rows:
            matrix[r] = [0] * cols

        for c in zero_cols:
            for r in range(rows):
                matrix[r][c] = 0



        

        