# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow.next
        slow.next = None

        prev = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        head2 = prev
        head1 = head

        while head2:
            temp1 = head1.next
            temp2 = head2.next
            
            head1.next = head2
            head2.next = temp1
            
            head1 = temp1
            head2 = temp2
