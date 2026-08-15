class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2

        dp = set([0])
        for num in nums:
            new_dp = set()
            for prev_num in dp:
                new_num = prev_num + num
                if new_num == half:
                    return True
                new_dp.add(prev_num)
                if new_num < half:
                    new_dp.add(new_num)
            dp = new_dp
        
        return False
            
                
