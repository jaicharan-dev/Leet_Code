# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        min_heap = []

        for idx, linked_list_head in enumerate(lists):
            if linked_list_head:
                heapq.heappush(min_heap, (linked_list_head.val, idx, linked_list_head))
        next_idx = len(lists)

        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, next_idx, node.next))
                next_idx += 1
        return dummy.next