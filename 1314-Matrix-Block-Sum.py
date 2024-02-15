class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        answer = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                for r in range(max(0, i - k), min(rows, i + k + 1)):
                    for c in range(max(0, j - k), min(cols, j + k + 1)):
                        answer[i][j] += mat[r][c]

        return answer