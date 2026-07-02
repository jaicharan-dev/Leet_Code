class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            diff = current_sum - k

            if diff in prefix_sum:
                count += prefix_sum[diff]

            prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum, 0)
        return count