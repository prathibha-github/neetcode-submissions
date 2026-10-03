# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(None)
        current = result
        carry = 0
        output = 0
        while l1 and l2:
            output = l1.val + l2.val + carry
            if output >= 10:
                output = output % 10
                carry = 1
            else:
                carry = 0
            outputNode = ListNode(output, None)
            current.next = outputNode
            current = current.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            output = l1.val + carry
            if output >= 10:
                output = output % 10
                carry = 1
            else:
                carry = 0
            outputNode = ListNode(output, None)
            current.next = outputNode
            current = current.next
            l1 = l1.next

        while l2:
            output = l2.val + carry
            if output >= 10:
                output = output % 10
                carry = 1
            else:
                carry = 0
            outputNode = ListNode(output, None)
            current.next = outputNode
            current = current.next
            l2 = l2.next
        
        if carry == 1:
            outputNode = ListNode(carry, None)
            current.next = outputNode
            current = current.next

        return result.next
        
