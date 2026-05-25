class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1 , max(piles)

        while l <= r:
            bananas_per_hr = (l + r) // 2
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / bananas_per_hr) 
            
            if time_taken <= h:
                r = bananas_per_hr - 1
            else: # time_taken > hr
                l = bananas_per_hr + 1
        
        return l
        

