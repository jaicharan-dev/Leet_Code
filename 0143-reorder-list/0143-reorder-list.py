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
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        curr, prev, slow.next = slow.next, None, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        head1, head2 = dummy.next, prev
        while head2:
            head1.next,head2.next,head1,head2=head2,head1.next,head1.next,head2.next
        return dummy.next