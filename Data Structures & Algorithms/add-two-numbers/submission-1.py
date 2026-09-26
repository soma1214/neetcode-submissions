# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        t1=l1
        t2=l2
        carry=0
        while t1 is not None or t2 is not None or carry:
            sum=carry
            if t1:
                sum+=t1.val
                t1=t1.next
            if t2:
                sum+=t2.val
                t2=t2.next
            newNode=ListNode(sum%10)
            carry=sum//10
            curr.next=newNode
            curr=curr.next
        
        if carry:
            newNode=ListNode(carry)
            curr.next=carry
        return dummy.next
        