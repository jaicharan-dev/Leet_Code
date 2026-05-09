class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1

        while left < right:
            curr_area = (right-left) * min(height[left], height[right])
            max_area = max(max_area, curr_area)
            
            temp_left = height[left]
            temp_right = height[right]
            
            if height[left] == height[right]:
                while left < right and height[left] <= temp_left:
                    left += 1
                while left < right and height[right] <= temp_right:
                    right -= 1
            
            elif height[left] < height[right]:
                while left < right and height[left] <= temp_left:
                    left += 1
            else:
                while left < right and height[right] <= temp_right:
                    right -= 1
        return max_area
