class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        can_possible = [False] * n
        can_possible[n-1] = True

        for i in range(n-2, -1, -1):
            for j in range(i+1, i+1+nums[i]):
                if j < n and can_possible[j] == True:
                    can_possible[i] = True
                    break
        
        return can_possible[0] == True