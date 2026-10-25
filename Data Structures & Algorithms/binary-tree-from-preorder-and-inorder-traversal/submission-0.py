# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inmap={}

        for i in range(len(inorder)):
            inmap[inorder[i]]=i
        

        root=self.buildtree(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,inmap)

        return root
    
    def buildtree(self,preorder,prestart,preend,inorder,instart,inend,inmap):

        if prestart>preend or instart>inend:
            return None
        
        root=TreeNode(preorder[prestart])

        inroot=inmap[root.val]

        numsleft=inroot-instart

        root.left=self.buildtree(preorder,prestart+1,prestart+numsleft,inorder,instart,inroot-1,inmap)

        root.right=self.buildtree(preorder,prestart+numsleft+1,preend,inorder,inroot+1,inend,inmap)

        return root
    