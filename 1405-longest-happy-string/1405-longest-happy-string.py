class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        res = []
        # lets make the heap, 
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
        # but it should not have any element if it has zero freq
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
        # there are only two cases when we would have to stop
        # first is when the maxheap is exhausted
        # in other words the max freq we are permiited to use is fully exhausted
        # there is no way we can make a longer string than the upper limit
        # so we run our will loop still complete exhaustion
        # second is triple streak, if we have double streak
        # and there is no other element in the heap to break the streak we must stop
        # that is handled inside the while loop
        while maxHeap:
            # let pop our highest frequency element to append to res
            count, char = heapq.heappop(maxHeap)
            # before appending we need to check for double streak
            # if yes - then append after another element 
            # if not - then happily append it now itself
            # a situation where we can't use the maximum element
            # already double streak
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                # since it is already used twice
                # use the second most frequent element
                # but for the the heap must exist
                # if the heap is empty, we can't proceed further
                if not maxHeap:
                    break # the end ( just return the result after this )
                
                # if heap exists then we are lucky, we can break the double streak
                # pop the second most frequent element
                count2, char2 = heapq.heappop(maxHeap)
                # i have a question here, why did we pop the first element in the beginning itself
                # if we are not sure whether we will use it or not
                # the answer is, where we use it or not we have to pop it
                # suppose we dont use it, then we need the next element, 
                # but we cant access that without popping this,
                # hence we just pop it either way and append back if not needed
                # it is not very time consuming as our heap has max length of 3
                # so log3 = O(1), so not a problem
                # anyways, now we have the second char, go ahead and append it to res
                res.append(char2)
                # now we reduce its count by 1
                count2 += 1
                # since it -ve, +1 reduces it overall count 
                # if it not exhausted to zero, push back to heap
                if count2 != 0:
                    heapq.heappush(maxHeap, (count2, char2))
                # don't forget our first element is still out
                # its has not been used yet and can be used now
                # i think we need not puch back to heap now,
                # it is surely the next element to add to our result
                # as it has the highest freq
                res.append(char)
                # reduce the count
                count += 1
                # if the element is not exhausted to zero, append back to heap
                if count != 0:
                    heapq.heappush(maxHeap, (count, char))
            # we can use the max element
            else:
                # just append to our res with no worries
                res.append(char)
                # reduce the count as we used it once
                count += 1
                # if the count in not zero
                # means the char is still no used fully
                if count != 0:
                    # push it back to the maxHeap
                    heapq.heappush(maxHeap, (count, char))
        return "".join(res)
            

                