# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp=head
        prevNode=None
        while temp:
            kthnode=self.getkthnode(temp,k)
            if not kthnode:
                if prevNode:
                    prevNode.next=temp
                break
            nextnode=kthnode.next
            kthnode.next=None
            self.reverse(temp)
            if temp==head:
                head=kthnode
            else:
                prevNode.next=kthnode
            prevNode=temp
            temp=nextnode
        return head

    def getkthnode(self,curr,k):
        k-=1
        while curr and k>0:
            k-=1
            curr=curr.next
        return curr
    
    def reverse(self,temp):
        curr=temp
        prev=None
        while curr:
            front=curr.next
            curr.next=prev
            prev=curr
            curr=front
        return prev
        