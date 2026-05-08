class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                current_length = 1

                while (num + 1) in numSet:
                    num += 1
                    current_length += 1
                
                longest = max(current_length, longest)
        
        return longest
