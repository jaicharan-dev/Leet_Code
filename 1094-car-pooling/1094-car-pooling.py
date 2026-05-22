class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Determines if a car can successfully complete all pickup and drop-off 
        trips without ever exceeding its maximum passenger capacity.

        --- ALGORITHM STRATEGY: TIMELINE SIMULATION VIA SORTING & MIN-HEAP ---
        The core challenge is tracking the passenger load at any given coordinate 
        along the route. Instead of tracking every single mile, we only care about 
        discrete "events": when passengers get *in* the car, and when passengers 
        get *out* of the car.

        We process the timeline chronologically from left to right. Sorting handles 
        the order of pickups, while a Min-Heap manages the order of drop-offs.

        --- TIME & SPACE COMPLEXITY ---
        - Time Complexity: O(N log N), where N is the number of trips. 
          Sorting the trips array takes O(N log N). In the for-loop, each trip 
          is pushed onto and popped from the min-heap exactly once. Each heap 
          operation takes O(log N). Thus, the loop operations take O(N log N).
        - Space Complexity: O(N) to store the trips in the min-heap in the worst case 
          (e.g., if everyone gets picked up before anyone gets dropped off).
        """
        
        trips.sort(key=lambda x: x[1])
        minHeap = []
        i = 0
        n = len(trips)
        total_people = 0
        while i < n:
            # drop people
            while minHeap and minHeap[0][0] <= trips[i][1]:
                _, drop_people = heapq.heappop(minHeap)
                total_people -= drop_people
            # pick people
            num_people, start, end = trips[i]
            total_people += num_people
            # check capacity
            if total_people > capacity:
                return False
            # track next nearest drop
            heapq.heappush(minHeap, (end, num_people))
            # go to next start
            i += 1
        
        return True


        # firstly we will sort the trips based on their start
        # we move from left to right, so the one on the left we first pick
        # chronological ( time based ) processing: Sort trips by pickup stations (left to right)
        # allows jumping from station to station instead of simulating every single km
        
        # use a minheap to keep endpoint to drop people of
        # now we keep can increment one by one but that is very time taking, instead
        # lets just directly jump from one start point to another and pick up people
        # lets keep a track of num_people if exceeds capacity we can return false
            
            # i intially kept the adding step first, 
            # but then kept the substracting step first, because at every station
            # i want to check it the pick_people - drop people less than capacity or not
            # whenever there are no people to drop the while loop gets skipped anyways
        '''
        In carpooling, if 3 people are getting off at Mile 5, and 3 people are getting on at Mile 5, the old passengers step out of the vehicle first, freeing up seats before the new ones climb in. By putting the drop loop first, your code perfectly matches this reality.
        '''

            # so for each station, after checking if the people are dropped of earlier
            # i just want to append the start point in
            # instead of checking for every single km what my capacity
            # i will check my capacity only at the station points

            # after removing old people and adding new people
            # i have 2 important steps, to increment "i", that is go to next start point
            # and i need to push this endpoint to minHeap ( who knows it might be the earliest )
            # but before that a small optimization is to immidiately check for capacity
            # if at the current station the capacity excceeds we can stop here
            # saves us on heap push opperation


