# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None

        prev = None
        current = mid
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        second = prev
        first = head
        while second:
            first_next = first.next
            second_next = second.next
            
            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

        

