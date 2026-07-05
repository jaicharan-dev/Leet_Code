class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                is_alive = True
                while stack and stack[-1] > 0 and is_alive:
                    defender = stack.pop()
                    if defender > abs(asteroid):
                        stack.append(defender)
                        is_alive = False
                    elif defender == abs(asteroid):
                        is_alive = False
                if is_alive:
                    stack.append(asteroid)
        
        return stack

                    