class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p, s in zip(position, speed)]
        cars.sort()
        fleets = [] # stack (monotonic decreasing)

        for p, s in cars:
            time = (target - p) / s
            while fleets and time >= fleets[-1]:
                fleets.pop()
            fleets.append(time)

        return len(fleets)
        