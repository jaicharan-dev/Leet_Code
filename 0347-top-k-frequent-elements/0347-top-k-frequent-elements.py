class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n,0)

        pairs = []
        for num, freq in freqMap.items():
            pairs.append((freq, num))
        pairs.sort(reverse = True)

        res = []
        for i in range(k):
            res.append(pairs[i][1])
        return res

