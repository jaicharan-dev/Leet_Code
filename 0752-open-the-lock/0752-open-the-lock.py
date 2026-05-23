class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        Calculates the minimum number of total wheel turns required to open a 4-dial combination 
        lock from "0000" to a target code without hitting any deadends.

        --- ALGORITHM STRATEGY: SHORT-PATH GRAPH EXPLORATION (BFS) ---
        The combination lock can be viewed as an unweighted state-space graph containing exactly 
        10,000 nodes (combinations from "0000" to "9999"). Each node has exactly 8 neighboring 
        states (4 dials, each of which can be turned either up or down).

        Because all state transitions carry an identical weight of 1 turn, a standard 
        Breadth-First Search (BFS) is guaranteed to find the shortest path to the target.

        --- DATA ARCHITECTURE INSIGHTS ---
        1. UNIFIED FILTERING: We seed our `visited` set with all the `deadends`. Since deadends 
           are forbidden states, treating them as blocks we have "already visited" allows us to 
           use a single constant-time hash check to skip both deadends and loops.
        2. SHORT-CIRCUIT GUARD: If the starting sequence "0000" itself is a deadend, it is 
           impossible to make any legal moves. We catch this immediately.
        3. MODULO WRAPAROUND: (digit - 1) % 10 elegantly handles the wrap-around from 0 back to 9 
           due to Python's handling of negative modular math (e.g., -1 % 10 = 9).

        --- TIME & SPACE COMPLEXITY ---
        - Time Complexity: O(1) or bounded by O(D + A^N * N^2) where A is alphabet size (10), 
          N is number of dials (4). Practically, there are a constant maximum of 10,000 states. 
          For each state popped, we perform a string concatenation of length 4 across 8 variations. 
          This yields a hard upper limit of roughly 10,000 * 8 * 4 operations, which runs instantly.
        - Space Complexity: O(1) or bounded by O(A^N) to store the visited combinations and 
          the queue elements, which caps strictly at 10,000 records.
        """
        
        visited = set(deadends)

        if "0000" in visited:
            return -1
        
        queue = deque([("0000", 0)])
        visited.add("0000")

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
