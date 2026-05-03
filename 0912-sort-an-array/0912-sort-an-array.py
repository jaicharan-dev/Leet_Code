class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid]) 
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        sort_arr = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sort_arr.append(left[i])
                i += 1
            else:
                sort_arr.append(right[j])
                j += 1
        
        sort_arr.extend(left[i:])
        sort_arr.extend(right[j:])
        
        return sort_arr


