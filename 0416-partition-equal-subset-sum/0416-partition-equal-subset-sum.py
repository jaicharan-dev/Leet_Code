class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        dp = {0}
        
        for num in nums:
            next_dp = set()
            for curr_sum in dp:
                next_dp.add(curr_sum)
                new_sum = curr_sum + num
                if new_sum == target: return True
                if new_sum < target: next_dp.add(new_sum)
            
            dp = next_dp

        return target in dp