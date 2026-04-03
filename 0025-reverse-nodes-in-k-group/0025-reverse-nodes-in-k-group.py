# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self._get_kth(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = group_prev.next
            group_prev.next = prev
            group_prev = tmp
        return dummy.next
    
    def _get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr