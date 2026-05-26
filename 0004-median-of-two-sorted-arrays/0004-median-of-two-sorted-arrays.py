class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = (total + 1) // 2

        # Ensure A is the smaller array to optimize time complexity to O(log(min(M, N)))
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A)

        while l <= r:
            i = (l + r) // 2  # Partition index for A
            j = half - i      # Partition index for B

            # Grab boundary elements, handle edge cases with infinity if partition is at the ends
            A_left = A[i - 1] if i > 0 else float('-inf')
            A_right = A[i] if i < len(A) else float('inf')
            
            B_left = B[j - 1] if j > 0 else float('-inf')
            B_right = B[j] if j < len(B) else float('inf')

            # Check if partition is correct
            if A_left <= B_right and B_left <= A_right:
                # Odd total number of elements: median is the max of the left halves
                if total % 2 != 0:
                    return max(A_left, B_left)
                # Even total number of elements: average of the two middle elements
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
                
            elif A_left > B_right:
                # Too many elements from A, move left bound down
                r = i - 1
            else:
                # Too few elements from A, move right bound up
                l = i + 1