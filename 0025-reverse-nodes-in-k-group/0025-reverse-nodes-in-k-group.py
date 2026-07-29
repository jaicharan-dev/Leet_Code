# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if k exist in the first place, needs to be checked and then we can thinki of swapping
        dummy = ListNode(0, head)
        gp = dummy

        def is_k(node):
            count = 0
            while node.next:
                node = node.next
                count += 1
                if count == k:
                    return True
            return False

        while is_k(gp):
            curr = gp.next
            for _ in range(k-1):
                temp = curr.next
                curr.next = temp.next
                temp.next = gp.next
                gp.next = temp
            gp = curr
        
        return dummy.next