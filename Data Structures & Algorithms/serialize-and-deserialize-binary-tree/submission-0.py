# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""
        
        s=""
        queue=deque([root])
        while queue:
            currnode=queue.popleft()

            if currnode is None:
                s+="#,"
            else:
                s+=str(currnode.val)+","
            
            if currnode:
                queue.append(currnode.left)
                queue.append(currnode.right)
        
        return s
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if not data:
            return None
        
        s=data.split(",")

        root=TreeNode(int(s[0]))

        queue=deque([root])

        i=1

        while queue:

            node=queue.popleft()

            if s[i]=="#":
                node.left=None
            else:

                leftnode=TreeNode(int(s[i]))
                node.left=leftnode
                queue.append(leftnode)
            
            i+=1

            ##Right child

            if s[i]=="#":
                node.right=None
            else:
                rightnode=TreeNode(int(s[i]))
                node.right=rightnode
                queue.append(rightnode)
            i+=1
        return root
