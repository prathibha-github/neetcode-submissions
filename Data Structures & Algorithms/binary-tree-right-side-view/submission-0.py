# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        def level_order(root):
            current_layer = [root]
            while current_layer:
                next_layer = []
                result.append(current_layer[-1].val)
                for node in current_layer:
                    if node.left:
                        next_layer.append(node.left)
                    if node.right:
                        next_layer.append(node.right)
                current_layer = next_layer
            
        level_order(root)
        return result