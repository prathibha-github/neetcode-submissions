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
        dictionary = {}
        current = head
        while current:
            node = Node(current.val)
            dictionary[current] = node
            current = current.next

        current = head
        dummy = Node(0)
        newList = dummy
        while current:
            node = dictionary[current]
            newList.next = node
            if current.next == None:
                nodeNext = None
            else:
                nodeNext = dictionary[current.next]
            node.next = nodeNext
            
            if current.random == None:
                nodeRandom = None
            else:
                nodeRandom = dictionary[current.random]
            node.random = nodeRandom
            
            current = current.next
            newList = newList.next
        return dummy.next
