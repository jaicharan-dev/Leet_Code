class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        rob1 = self.dp(nums[:-1])
        rob2 = self.dp(nums[1:])

        return max(rob1, rob2)

    def dp(self, houses):
        if len(houses) == 1: return houses[0]
        if len(houses) == 2: return max(houses[0], houses[1])

        two_back, one_back = houses[0], max(houses[0], houses[1])

        for i in range(2, len(houses)):
            curr = max(two_back + houses[i], one_back)
            two_back = one_back
            one_back = curr
        
        return one_back