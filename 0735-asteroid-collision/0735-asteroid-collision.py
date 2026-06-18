class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            
            if asteroid < 0:
                alive = True
                while alive and stack and stack[-1] > 0:
                    prev = stack.pop()
                    if abs(asteroid) < prev:
                        alive = False
                        stack.append(prev)
                    elif abs(asteroid) == prev:
                        alive = False
                if alive:
                    stack.append(asteroid)

            else:
                stack.append(asteroid)

        return stack