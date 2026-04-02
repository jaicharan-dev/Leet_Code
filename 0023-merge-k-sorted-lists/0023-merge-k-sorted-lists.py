# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        min_heap = []
        
        for index, linked_list_head, in enumerate(lists):
            if linked_list_head:
                heapq.heappush(min_heap, (linked_list_head.val, index, linked_list_head))
        
        next_index = len(lists)
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, next_index, node.next))
                next_index += 1
        return dummy.next

