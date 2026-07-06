# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gl = dummy

        for _ in range(left-1):
            gl = gl.next
        
        curr = gl.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = gl.next
            gl.next = temp
            
        return dummy.next

        
