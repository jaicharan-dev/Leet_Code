class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def count_days(ship_capacity):
            curr_capacity = 0
            i = 0
            days = 1
            while i < len(weights):
                if curr_capacity + weights[i] <= ship_capacity:
                    curr_capacity += weights[i]
                else:
                    days += 1
                    curr_capacity = weights[i]
                i += 1
            return days

        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2
            days_taken = count_days(mid)
            if days_taken <= days:
                right = mid - 1
            else:
                left = mid + 1 
        return left


