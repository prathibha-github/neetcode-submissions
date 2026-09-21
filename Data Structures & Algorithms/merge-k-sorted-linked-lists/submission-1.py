# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for list_index, list_head in enumerate(lists):
            if list_head:
                heapq.heappush(heap, (list_head.val, list_index, list_head))
        dummy = ListNode(0, None)
        current = dummy
        while heap:
            val, list_id, node = heapq.heappop(heap)
            current.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, list_id, node.next))
            current = current.next
        return dummy.next