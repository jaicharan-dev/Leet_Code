class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a < 0:
                alive = True
                while alive and stack and stack[-1] > 0:
                    if stack[-1] < abs(a):
                        stack.pop()
                    elif stack[-1] == abs(a):
                        stack.pop()
                        alive = False
                    else:
                        alive = False
                if alive:
                    stack.append(a)
            else:
                stack.append(a)
        return stack
