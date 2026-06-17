class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        cnt = 1
        for i in range(1,len(nums)):
            if nums[i] != curr:
                cnt -= 1
                if cnt == 0:
                    curr = nums[i]
                    cnt = 1
            else:
                cnt += 1 
        return curr