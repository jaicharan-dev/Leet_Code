class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        boats = 0

        while left <= right:
            boats += 1
            if left == right:
                break
            elif people[left] + people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1

        return boats

