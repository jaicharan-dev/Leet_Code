class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
            
        if not matrix or not matrix[0]:
            return 0
            
        cols = len(matrix[0])
        
        # Step 1: Initialize our three 1D state arrays
        height = [0] * cols
        left = [0] * cols
        right = [cols] * cols # Initialize right boundaries to the far right edge
        
        max_area = 0
        
        # Step 2: Process row by row
        for row in matrix:
            cur_left = 0
            cur_right = cols
            
            # Update height
            for c in range(cols):
                if row[c] == '1':
                    height[c] += 1
                else:
                    height[c] = 0
                    
            # Update left boundary (scan left to right)
            for c in range(cols):
                if row[c] == '1':
                    left[c] = max(left[c], cur_left)
                else:
                    left[c] = 0
                    cur_left = c + 1
                    
            # Update right boundary (scan right to left)
            for c in range(cols - 1, -1, -1):
                if row[c] == '1':
                    right[c] = min(right[c], cur_right)
                else:
                    right[c] = cols
                    cur_right = c
                    
            # Step 3: Calculate the maximum area for the current row's histogram
            for c in range(cols):
                # Area = height * width
                area = height[c] * (right[c] - left[c])
                max_area = max(max_area, area)
                
        return max_area