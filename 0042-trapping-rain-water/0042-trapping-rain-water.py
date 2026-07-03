class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        left_wall, right_wall = height[left], height[right]
        trapped = 0

        while left <= right:
            if left_wall <= right_wall:
                water = left_wall - height[left]
                if water > 0:
                    trapped += water
                else:
                    left_wall = height[left]
                left += 1
            else:
                water = right_wall - height[right]
                if water > 0:
                    trapped += water
                else:
                    right_wall = height[right]
                right -= 1
        
        return trapped
