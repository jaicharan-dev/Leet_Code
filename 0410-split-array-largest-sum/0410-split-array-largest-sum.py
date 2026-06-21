class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def can_split(max_sum):
            curr_sum = 0
            subarray_cnt = 1

            for num in nums:
                curr_sum += num

                if curr_sum > max_sum:
                    subarray_cnt += 1
                    curr_sum = num
            return subarray_cnt <= k
        
        low, high = max(nums), sum(nums)
        best_limit = high

        while low <= high:
            mid = (low + high) // 2
            if can_split(mid):
                best_limit = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return best_limit

