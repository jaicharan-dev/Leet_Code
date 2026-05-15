class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        total_passengers = [0] * 1001
        curr_passengers = 0
        for num_passengers, start, end in trips:
            total_passengers[start] += num_passengers
            total_passengers[end] -= num_passengers
        for passengers in total_passengers:
            curr_passengers += passengers
            if curr_passengers > capacity:
                return False
        return True
