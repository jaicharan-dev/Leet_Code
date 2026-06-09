class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {char:i for i, char in enumerate(s)}

        res = []
        start = 0 
        end = 0

        for i, char in enumerate(s):
            end = max(end, last_index[char])

            if i == end:
                size = end - start + 1
                res.append(size)
                start = i + 1

        return res