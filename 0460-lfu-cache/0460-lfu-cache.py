class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val_freq = {}
        self.freq_to_key = defaultdict(dict)
        self.min_freq = 0

    def _update_freq(self, key, freq):
        del self.freq_to_key[freq][key]
        if freq == self.min_freq and not self.freq_to_key[freq]:
            self.min_freq += 1
        
        new_freq = freq + 1
        self.key_to_val_freq[key][1] = new_freq
        self.freq_to_key[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        val, freq = self.key_to_val_freq[key]
        self._update_freq(key, freq)
        return val
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key][0] = value
            freq = self.key_to_val_freq[key][1]
            self._update_freq(key, freq)
        else:
            if len(self.key_to_val_freq) >= self.capacity:
                lru_key = next(iter(self.freq_to_key[self.min_freq]))
                del self.key_to_val_freq[lru_key]
                del self.freq_to_key[self.min_freq][lru_key]
            
            self.key_to_val_freq[key] = [value, 1]
            self.freq_to_key[1][key] = None
            self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)