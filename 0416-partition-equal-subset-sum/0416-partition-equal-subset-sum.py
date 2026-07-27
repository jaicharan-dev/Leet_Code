class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        half = sum(nums) // 2 
        dp = {0}

        for num in nums:
            next_dp = set()
            for curr_sum in dp:
                new_sum = curr_sum + num
                next_dp.add(curr_sum)
                if new_sum == half: return True
                if new_sum < half: next_dp.add(new_sum)
            
            dp = next_dp
        
        return half in dp