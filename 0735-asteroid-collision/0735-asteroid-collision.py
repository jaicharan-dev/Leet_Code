class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                flag = True
                while flag and stack and stack[-1] > 0:
                    defender = stack.pop()
                    if defender > abs(asteroid):
                        flag = False
                        stack.append(defender)
                    elif defender == abs(asteroid):
                        flag = False
                
                if flag:
                    stack.append(asteroid)
        
        return stack
                
