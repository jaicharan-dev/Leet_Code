class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0

        left = 0 
        right = len(people)-1

        while left <= right:
            boats += 1
            space_remaining = limit - people[right]
            right -= 1

            if left <= right and space_remaining >= people[left]:
                left += 1
        
        return boats 