class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Calculates the longest possible "happy" string using the available counts of 
        characters 'a', 'b', and 'c'. A string is happy if it does not contain 
        three consecutive identical characters (e.g., 'aaa', 'bbb', 'ccc' are banned).

        --- ALGORITHM STRATEGY: GREEDY WITH MAX-HEAP ---
        The fundamental rule of this problem is to always burn through the most 
        abundant character first. If we don't, that dominant character will get 
        left behind, and we will eventually run out of other characters to separate 
        it, forcing an early termination. 

        To constantly fetch the most abundant character in O(log N) time, we utilize 
        a Max-Heap.

        --- TIME & SPACE COMPLEXITY ---
        - Time Complexity: O(a + b + c). In the worst-case scenario, we process 
          every single character. Each heap operation (push/pop) takes O(log 3) 
          time because the heap never holds more than 3 elements. Since O(log 3) 
          is a constant O(1), the overall time scales linearly with the character counts.
        - Space Complexity: O(1) auxiliary space, as the heap size is strictly 
          bounded to a maximum of 3 elements. The output list takes O(a + b + c) 
          space to store the resulting string.
        """

        maxHeap = []
        res = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not maxHeap:
                    break # the end ( just return the result after this )
                
                count2, char2 = heapq.heappop(maxHeap)
                res.append(char2)
                count2 += 1
                if count2 != 0:
                    heapq.heappush(maxHeap, (count2, char2))
                res.append(char)
                count += 1
                if count != 0:
                    heapq.heappush(maxHeap, (count, char))
            else:
                res.append(char)
                count += 1
                if count != 0:
                    heapq.heappush(maxHeap, (count, char))
        return "".join(res)
        
        # lets make the heap, 
        # but it should not have any element if it has zero freq
        # there are only two cases when we would have to stop
        # first is when the maxheap is exhausted
        # in other words the max freq we are permiited to use is fully exhausted
        # there is no way we can make a longer string than the upper limit
        # so we run our will run while loop still complete exhaustion
        # second is triple streak, if we have double streak
        # and there is no other element in the heap to break the streak we must stop
        # that is handled inside the while loop
            # let pop our highest frequency element to append to res
            # before appending we need to check for double streak
            # if yes - then append after another element 
            # if not - then happily append it now itself
            # a situation where we can't use the maximum element
            # already double streak
                # since it is already used twice
                # use the second most frequent element
                # but for the the heap must exist
                # if the heap is empty, we can't proceed further
                # if heap exists then we are lucky, we can break the double streak
                # pop the second most frequent element
                # i have a question here, why did we pop the first element in the beginning itself
                # if we are not sure whether we will use it or not
                # the answer is, where we use it or not we have to pop it
                # suppose we dont use it, then we need the next element, 
                # but we cant access that without popping this,
                # hence we just pop it either way and append back if not needed
                # it is not very time consuming as our heap has max length of 3
                # so log3 = O(1), so not a problem
                # anyways, now we have the second char, go ahead and append it to res
                # now we reduce its count by 1
                # since it -ve, +1 reduces it overall count 
                # if it not exhausted to zero, push back to heap
                # don't forget our first element is still out
                # its has not been used yet and can be used now
                # i think we need not puch back to heap now,
                # it is surely the next element to add to our result
                # as it has the highest freq
                # reduce the count
                # if the element is not exhausted to zero, append back to heap
            # we can use the max element
                # just append to our res with no worries
                # reduce the count as we used it once
                # if the count in not zero
                # means the char is still no used fully
                    # push it back to the maxHeap
            

                