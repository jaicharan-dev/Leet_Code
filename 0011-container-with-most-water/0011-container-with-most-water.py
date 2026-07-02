class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_water = 0

        while left < right:
            curr_water = (right - left) * min(height[left], height[right])
            max_water = max(max_water, curr_water)

            if height[left] <= height[right]:
                while left < right and height[left] >= height[left + 1]:
                    left += 1
                left += 1

            else:
                while left < right and height[right] >= height[right - 1]:
                    right -= 1
                right -= 1
        
        return max_water

