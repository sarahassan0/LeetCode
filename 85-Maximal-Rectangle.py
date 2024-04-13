class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        maxArea = 0
        histogram = [0] * len(matrix[0]) 
        
        for row in matrix:
            for col in range(cols):
                if row[col] == '0':
                    histogram[col] = 0
                else:
                    histogram[col] += 1
            
            print(histogram)
            
            stack = []
            for i, h in enumerate(histogram+[0]):  
                start = i
                while stack and h < stack[-1][1]:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i - index))
                    start = index
                stack.append((start,h))
        
        return maxArea