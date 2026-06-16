class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        curr = m+n-1
        arr1 = m-1
        arr2 = n-1

        while arr2 >= 0:
            if arr1 >= 0 and nums1[arr1] > nums2[arr2]:
                nums1[curr] = nums1[arr1]
                curr -= 1
                arr1 -= 1
            else:
                nums1[curr] = nums2[arr2]
                curr -= 1
                arr2 -= 1
        