class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])

        height = [0] * cols
        left = [0] * cols
        right = [cols] * cols

        max_area = 0

        for row in matrix:
            cur_left = 0
            cur_right = cols

            for c in range(cols):
                if row[c] == '1':
                    height[c] += 1
                else:
                    height[c] = 0
            
            for c in range(cols):
                if row[c] == '1':
                    left[c] = max(left[c], cur_left)
                else:
                    left[c] = 0
                    cur_left = c+1
            
            for c in range(cols-1, -1, -1):
                if row[c] == '1':
                    right[c] = min(right[c], cur_right)
                else:
                    right[c] = cols
                    cur_right = c
            
            for c in range(cols):
                cur_area = height[c] * (right[c] - left[c])
                max_area = max(max_area, cur_area)
        
        return max_area

