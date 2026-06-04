class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_back = 0
        two_back = 0

        for i in range(2, len(cost)+1):
            take_one_step = one_back + cost[i-1]
            take_two_step = two_back + cost[i-2]

            current = min(take_one_step, take_two_step)

            two_back = one_back
            one_back = current
        
        return one_back