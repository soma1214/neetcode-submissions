"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def insertcopyinbetween(self,head):
        temp=head
        while temp:
            copynode=Node(temp.val)
            copynode.next=temp.next
            temp.next=copynode
            temp=temp.next.next
        
    def connectrandompointers(self,head):
        temp=head
        while temp:
            copynode=temp.next
            if temp.random:
                copynode.random=temp.random.next
            else:
                copynode.random=None
            temp=temp.next.next
        
    def getdeepcopy(self,head):
        temp=head
        dummy=Node(-1)
        res=dummy
        while temp:
            res.next=temp.next
            temp.next=temp.next.next
            res=res.next
            temp=temp.next
        return dummy.next
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """if not head:
            return None

        
        temp=head
        mpp={}
        while temp:
            newnode=Node(temp.val)
            mpp[temp]=newnode
            temp=temp.next
        temp=head
        while temp:
            copynode=mpp[temp]
            copynode.next=mpp.get(temp.next)
            copynode.random=mpp.get(temp.random)
            temp=temp.next
        return mpp[head]"""

        self.insertcopyinbetween(head)
        self.connectrandompointers(head)
        return self.getdeepcopy(head)



        