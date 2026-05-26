class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        def can_split(max_sum):
            pieces = 1
            current_sum = 0

            for num in nums:
                if current_sum + num <= max_sum:
                    current_sum += num
                else:
                    pieces += 1
                    current_sum = num
            return pieces
        
        while left <= right:
            mid = (left + right) // 2
            if can_split(mid) <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left