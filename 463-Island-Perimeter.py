class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for r in range(len(grid)):
            perimeter += sum( grid[r]) * 4 

            for c in range(len(grid[r])):
                
                if c > 0  and  grid[r][c-1] == 1 == grid[r][c] :
                    perimeter -= 2

                if r > 0  and  grid[r-1][c] == 1 == grid[r][c] :
                    perimeter -= 2
        
        return perimeter