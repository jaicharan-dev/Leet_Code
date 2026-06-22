# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev_left = dummy

        for _ in range(left-1):
            prev_left = prev_left.next
        
        curr = prev_left.next
        for _ in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev_left.next
            prev_left.next = temp
        
        return dummy.next
