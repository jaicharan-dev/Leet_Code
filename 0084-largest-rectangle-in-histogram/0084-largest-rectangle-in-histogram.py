class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0
        for idx, height in enumerate(heights):
            prev_idx = None
            while stack and stack[-1][0] > height:
                prev_height, prev_idx = stack.pop() 
                max_area = max(max_area, prev_height * (idx - prev_idx))
            if prev_idx != None:
                idx = prev_idx
            stack.append((height, idx))
        return max_area