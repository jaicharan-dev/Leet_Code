# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy 
        for _ in range(left):
            cur = cur.next

        prev = cur
        cur = cur.next
        nxt = None
        for _ in range(right-left):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        cur2 = dummy
        for _ in range(left-1):
            cur2 = cur2.next
        
        temp = cur2.next
        cur2.next = prev
        temp.next = cur

        return dummy.next
