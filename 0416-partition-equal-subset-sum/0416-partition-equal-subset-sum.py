class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = set()
        dp.add(0)

        for n in nums:
            next_dp = set()
            for current_sum in dp:
                new_sum = current_sum + n
                if new_sum == target:
                    return True
                next_dp.add(new_sum)
                next_dp.add(current_sum)
            dp = next_dp
        return False
                
                
