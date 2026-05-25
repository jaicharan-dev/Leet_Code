class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        sequence = self.timeMap[key]
        l, r = 0, len(sequence)-1
        while l <= r:
            mid = (l+r) // 2
            time = sequence[mid][0]
            if time == timestamp:
                return sequence[mid][1]
            elif time < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return sequence[r][1] if r >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)