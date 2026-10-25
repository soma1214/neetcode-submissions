# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxi=float('-inf')

        def maxpath(node):

            nonlocal maxi
            if node is None:
                return 0

            leftsum=max(0,maxpath(node.left))
            rightsum=max(0,maxpath(node.right))

            maxi=max(maxi,leftsum+rightsum+node.val)

            return max(leftsum,rightsum)+node.val
        
        maxpath(root)
        return maxi
        