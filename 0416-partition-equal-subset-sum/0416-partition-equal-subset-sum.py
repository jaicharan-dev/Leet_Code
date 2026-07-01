class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = set()
        dp.add(0)

        for n in nums:
            new_dp = set()
            for prev_sum in dp:
                new_sum = n + prev_sum
                if new_sum == target: 
                    return True
                new_dp.add(prev_sum)
                new_dp.add(new_sum)
            dp = new_dp
        
        return False