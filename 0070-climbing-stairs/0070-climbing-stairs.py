class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        two_back = 1
        one_back = 2

        for i in range(3, n+1):
            current = one_back + two_back
            two_back = one_back
            one_back = current

        return one_back    