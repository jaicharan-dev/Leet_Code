class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def num_days(capacity):
            days_needed = 1
            weight_in_ship = 0
            for weight in weights:
                if weight_in_ship + weight <= capacity:
                    weight_in_ship += weight
                else:
                    days_needed += 1
                    weight_in_ship = weight            
            return days_needed

        while left <= right:
            mid = (left + right) // 2 # capacity
            days_taken = num_days(mid)
            if days_taken <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left