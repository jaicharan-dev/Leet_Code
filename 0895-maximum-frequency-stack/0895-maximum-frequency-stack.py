class FreqStack:

    def __init__(self):
        self.freq_map = Counter()
        self.group_map = defaultdict(list)
        self.max_freq = 0
        
    def push(self, val: int) -> None:
        self.freq_map[val] += 1
        current_freq = self.freq_map[val]

        if current_freq > self.max_freq:
            self.max_freq = current_freq
        
        self.group_map[current_freq].append(val)
        
    def pop(self) -> int:
        val = self.group_map[self.max_freq].pop()
        self.freq_map[val] -= 1

        if not self.group_map[self.max_freq]:
            self.max_freq -= 1
        
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()