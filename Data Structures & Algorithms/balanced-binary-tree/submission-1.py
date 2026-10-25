# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):

            if not node:
                return 0

            lh=height(node.left)
            rh=height(node.right)

            if lh==-1 or rh==-1:
                return -1
            
            if abs(rh-lh)>1:
                return -1   
            
            return 1+max(lh,rh)

        if height(root)==-1:
            return False
        else:
            return True
        
        