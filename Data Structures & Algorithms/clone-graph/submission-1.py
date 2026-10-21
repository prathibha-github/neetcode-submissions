"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        copies = {}

        def clone(current):
            if current in copies:
                return copies[current]
            
            copy = Node(current.val)
            copies[current] = copy

            for neighbor in current.neighbors:
                copy.neighbors.append(clone(neighbor))
            
            return copy
    
        return clone(node)
            
        