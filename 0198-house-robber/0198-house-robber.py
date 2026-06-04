class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for n in nums:
            current = max(n+rob1, rob2)

            rob1 = rob2
            rob2 = current

        return rob2