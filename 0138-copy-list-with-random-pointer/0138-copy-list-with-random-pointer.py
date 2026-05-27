"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':     
        '''
        if not head:
            return None
        
        # 1. Interleave cloned nodes within the original list
        cur = head
        while cur:
            nxt = cur.next
            copy = Node(cur.val)
            cur.next = copy
            copy.next = nxt
            cur = nxt
            
        # 2. Assign random pointers to the cloned nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        # 3. Separate the interleaved lists
        cur = head
        dummy = Node(0)
        copy_curr = dummy
        
        while cur:
            nxt = cur.next.next
            
            # Extract the copy
            copy = cur.next
            copy_curr.next = copy
            copy_curr = copy
            
            # Restore the original link
            cur.next = nxt
            cur = nxt
            
        return dummy.next
        '''
        
        cur = head
        old_to_new = {None:None}

        while cur:
            if cur not in old_to_new:
                copy = Node(cur.val)
                old_to_new[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = old_to_new[cur]
            copy.next = old_to_new[cur.next]
            copy.random = old_to_new[cur.random]
            cur = cur.next
        
        return old_to_new[head]

        