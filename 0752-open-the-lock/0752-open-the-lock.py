class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadlock = set(deadends)
        if "0000" in deadlock:
            return -1

        q = deque([("0000", 0)])
        deadlock.add("0000")

        while q:
            state, step = q.popleft()
            if state == target:
                return step

            for i in range(4):
                digit = int(state[i])
                
                up_digit = str((digit - 1) % 10) 
                down_digit = str((digit + 1) % 10)

                up_state = state[:i] + up_digit + state[i+1:] 
                down_state = state[:i] + down_digit + state[i+1:]

                if up_state not in deadlock:
                    q.append((up_state, step+1))
                    deadlock.add(up_state)
                if down_state not in deadlock:
                    q.append((down_state, step+1))
                    deadlock.add(down_state)

        return -1
