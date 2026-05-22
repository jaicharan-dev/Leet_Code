class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Calculates the minimum number of minutes required for all fresh oranges 
        in a 2D grid to become rotten. If it is impossible, returns -1.

        --- ALGORITHM STRATEGY: MULTI-SOURCE BREADTH-FIRST SEARCH (BFS) ---
        The rot spreads from all rotten oranges simultaneously to their 4 adjacent 
        neighbors. This is a classic Multi-Source BFS where we track time by discrete 
        "minute layers".

        1. INITIAL MANIFEST: We traverse the grid once to log the initial coordinates 
           of all rotten oranges ('2') into a queue. At the same time, we count the total 
           number of fresh oranges ('1').
        2. LAYER-BY-LAYER PROCESSING: To track time accurately, we use a snapshot loop 
           `for _ in range(len(queue))`. This handles every orange currently rotten at this 
           exact minute mark simultaneously. Time only increments by +1 once the entire 
           current layer has completely finished expanding.
        3. EARLY STOPPING OPTIMIZATION: We run the loop while `queue and fresh > 0`. 
           Stopping the moment `fresh == 0` prevents the code from executing a final 
           "ghost iteration" that would incorrectly increment the timer an extra time 
           after all work is finished.

        --- TIME & SPACE COMPLEXITY ---
        - Time Complexity: O(R * C), where R is rows and C is columns. We inspect each cell 
          during the initialization phase. During the BFS, each cell is pushed and popped 
          from the queue at most once.
        - Space Complexity: O(R * C) auxiliary space required by the queue to store 
          rotten orange coordinates during worst-case infection spikes.
        """
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue and fresh > 0:
            time += 1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))
        
        return time if fresh == 0 else -1



        
        # we can use a multibfs approach for this problem
        # i will first find all the rotten oranges and keep them in a queue
        # we can pop them level by level
        # at each level, the fresh oranges to the adjacent will get rotten 
        # and time increments by one
        # i think we need to keep a count of all the frehs oranges as well
        # because some fresh oranges may not be reachable 
        # so once our queue ends we cant return time if any fresh orange remains

        # if grid not there return 0 
        # it takes 0 minutes to rotten 0 oranges
        # get the dimensions of the grid
        # initiate a queue
        # keep a track of fresh oranges and the time
        # first lets iterate all the grid points once
        # to find out the total number of fresh oranges 
        # and the coordinates of the rotten oranges
        # i dont get why do we need to keep the while loop on, if fresh > 0
''' Imagine you have a grid where the last remaining fresh orange gets infected at Minute 4.
That newly rotten orange is appended to the queue, and fresh drops from 1 to 0.
The loop finishes processing the current minute layer and jumps back up to the while condition.
If your condition was just while queue:, the code would look inside, 
see that there is still an orange sitting in the queue, and enter the loop again. 
It would immediately run time += 1, changing your timer from 4 to 5. 
Then, it would empty the queue, realize that this orange has no fresh neighbors left to infect, and terminate. 
You would accidentally return 5 minutes instead of 4! '''
            # the time increments the moment our rotten oranges infects others
            # we use a for loop to keep level difference
            # we increase the time not for every rotten orange that is popped
            # but for every level of rotten oranges
            # at one given level, all the rotten oranges are popped
                    # check bounds and uf the oranges is fresh
                    # if yes then make it rotten 
                    # and reduce the count of fresh oranges
                    # then add to list of rotten oranges
                    # this forms the next level of rotten oranges 
        # after spreading the infection, we can return the time it took to 
        # maximum spread the infection, after this there are still fresh oranges
        # then we can never spoil them like me
        # so we raise our hands and return -1


