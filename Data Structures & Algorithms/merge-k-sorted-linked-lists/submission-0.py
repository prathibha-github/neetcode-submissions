# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        dummy = ListNode(0, None)
        current = dummy
        while heap:
            val, id, node = heapq.heappop(heap)
            current.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, id, node.next))
            current = current.next
        return dummy.next