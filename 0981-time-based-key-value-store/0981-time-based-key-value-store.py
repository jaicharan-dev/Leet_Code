class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)      

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store: return ""

        time_list = self.store[key]
        left, right = 0, len(time_list)-1
        while left <= right:
            mid = (left + right) // 2
            if time_list[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return time_list[right][1] if right >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)