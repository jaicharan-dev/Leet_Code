class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = 0
        profit = 0
        for i in range(len(prices)-1, -1, -1):
            if cur_max < prices[i]:
                cur_max = prices[i] 
                for j in range(i):
                    profit = max(profit, cur_max - prices[j])
        return profit
