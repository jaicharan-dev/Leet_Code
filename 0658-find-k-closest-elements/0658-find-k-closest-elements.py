class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)-1

        while k < right-left+1:
            left_dist = abs(arr[left] - x)
            right_dist = abs(arr[right] - x)
            
            if (left_dist <= right_dist):
                right -= 1
            else:
                left += 1
            
        return arr[left:right+1]