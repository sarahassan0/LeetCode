class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        nagatives = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(i, j)
                if grid[i][j] < 0:
                    nagatives += 1

        return nagatives