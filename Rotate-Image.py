class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse the matrix
        for i in range(n):
            matrix[i] = matrix[i][::-1]

# matrix[i] = matrix[i][::-1] creates a copy of the row and reverses that. It will use O(n) space for the duration of the iteration, which would then be (presumably) garbage collected when the iteration is done. `matrix[i].reverse()` is in place and doesn't use the extra space (i.e. it's O(1)).


