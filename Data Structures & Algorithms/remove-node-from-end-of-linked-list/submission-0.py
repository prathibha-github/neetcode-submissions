# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        left = ListNode(0, head)
        dummy = left
        right = head
        while right and n > 0:
            right = right.next
            n = n - 1
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next
        
