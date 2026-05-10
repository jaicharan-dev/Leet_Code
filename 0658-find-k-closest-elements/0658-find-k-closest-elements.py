class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while (right - left + 1) > k:
            left_dist = abs(arr[left] - x)
            right_dist = abs(arr[right] - x)

            if left_dist <= right_dist:
                right -= 1
            else: # left_dist > right_dist:
                left += 1
        
        return arr[left:right+1]
                
