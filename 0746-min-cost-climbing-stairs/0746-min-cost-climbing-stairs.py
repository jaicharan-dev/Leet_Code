class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        
        one_back = cost[1]
        two_back = cost[0]

        for i in range(2, len(cost)):
            current_step = cost[i] + min(two_back, one_back)
            two_back = one_back
            one_back = current_step

        return min(one_back, two_back)
