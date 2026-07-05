class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res_cnt = 0
        prefix_sum = {0:1}
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            if diff in prefix_sum:
                res_cnt += prefix_sum[diff]
            prefix_sum[curr_sum] = 1 + prefix_sum.get(curr_sum, 0)

        return res_cnt    
