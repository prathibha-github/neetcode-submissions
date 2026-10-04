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
        if head is None:
            return head
        dictionary = {}
        current = head
        while current:
            node = Node(current.val)
            dictionary[current] = node
            current = current.next

        current = head
        while current:
            node = dictionary[current]
            if current.next == None:
                node.next = None
            else:
                node.next = dictionary[current.next]
            
            if current.random == None:
                node.random = None
            else:
                node.random = dictionary[current.random]
            current = current.next
        return dictionary[head]
