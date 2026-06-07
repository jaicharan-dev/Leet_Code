class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_a = False
        found_b = False
        found_c = False

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            if t[0] == target[0]:
                found_a = True
            if t[1] == target[1]:
                found_b = True
            if t[2] == target[2]:
                found_c = True

        return found_a and found_b and found_c