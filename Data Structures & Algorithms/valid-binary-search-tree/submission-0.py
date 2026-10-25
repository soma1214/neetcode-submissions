# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isvalidBST(root,float('-inf'),float('inf'))

    
    def _isvalidBST(self,root,minval,maxval):

        if root is None:
            return True
        
        if root.val>=maxval or root.val<=minval:
            return False
        
        return (self._isvalidBST(root.left,minval,root.val) and self._isvalidBST(root.right,root.val,maxval))