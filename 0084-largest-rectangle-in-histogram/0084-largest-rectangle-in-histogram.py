class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        max_area = 0
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > h:
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                max_area = max(max_area, curr_height * curr_width)
            stack.append(i)
        return max_area
