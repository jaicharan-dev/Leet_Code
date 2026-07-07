# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gL = dummy
        
        while True:
            gN = gL
            for _ in range(k):
                gN = gN.next
                if not gN:
                    return dummy.next
                    
            curr = gL.next
            for _ in range(k-1):
                temp = curr.next
                curr.next = temp.next
                temp.next = gL.next
                gL.next = temp
            gL = curr
            
            



