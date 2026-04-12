class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2

        left_part = self.sortArray(nums[:mid])
        right_part = self.sortArray(nums[mid:])
        return self.merge(left_part, right_part)


    def merge(self, left, right):
        sorted_arr = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])

        return sorted_arr

