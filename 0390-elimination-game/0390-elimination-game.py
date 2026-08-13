class Solution:
    def lastRemaining(self, n: int) -> int:
        remaining = n
        head = 0
        left_to_right = True
        step = 1
        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += step
            
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right
        return head+1
