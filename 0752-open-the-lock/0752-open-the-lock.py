class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1
            
        visited.add("0000")
        queue = deque([("0000", 0)])
        
        while queue:
            state, turns = queue.popleft()
            if state == target:
                return turns
            for i in range(4):
                digit = int(state[i])

                up_digit = str((digit + 1) % 10)
                down_digit = str((digit - 1) % 10)

                up_state = state[:i] + up_digit + state[i+1:]
                down_state = state[:i] + down_digit + state[i+1:]

                if up_state not in visited:
                    visited.add(up_state)
                    queue.append((up_state, turns+1))
                
                if down_state not in visited:
                    visited.add(down_state)
                    queue.append((down_state, turns+1))
        return -1
