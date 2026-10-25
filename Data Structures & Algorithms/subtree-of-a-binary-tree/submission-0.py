# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(node):
            if not node:
                return "#,"

            s = str(node.val) + ","
            s += serialize(node.left)
            s += serialize(node.right)

            return s

        root_str = serialize(root)
        sub_str = serialize(subRoot)

        return sub_str in root_str
