class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_min = prices[0]

        for price in prices:
            profit = price - curr_min
            if profit < 0:
                curr_min = price
            else:
                max_profit = max(max_profit, profit)
        
        return max_profit