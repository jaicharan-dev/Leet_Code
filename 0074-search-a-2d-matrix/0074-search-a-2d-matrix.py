class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the correct row
        ROWS, COLS = len(matrix), len(matrix[0])    
        
        l, r = 0, ROWS-1
        while l <= r:
            mid = (l+r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        row = r

        l, r = 0, COLS-1
        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False 
             