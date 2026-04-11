class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-1

        while (right-left+1) > k:
            dist_left = abs(arr[left]-x)
            dist_right = abs(arr[right]-x)

            if dist_left > dist_right:
                left += 1
            else:
                right -= 1
            
        return arr[left:right+1]
