class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return n

        one_back = 1
        two_back = 1

        for _ in range(2, n+1):
            one_back, two_back = one_back + two_back, one_back
        
        return one_back

