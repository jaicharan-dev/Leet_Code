class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        total_passengers = [0] * 1001
        for num_passengers, start, end in trips:
            for i in range(start, end):
                total_passengers[i] += num_passengers
        
        return max(total_passengers) <= capacity 
