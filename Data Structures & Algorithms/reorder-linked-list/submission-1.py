# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """if not head:
            return
        
        values=[]
        temp=head
        while temp:
            values.append(temp)
            temp=temp.next
        
        #reordered=[]

        left=0
        right=len(values)-1
        while left<right:
            left_next=values[left].next
            values[left].next=values[right]
            values[right].next=left_next
            left+=1
            right-=1
        values[left].next=None
        return """

        ##find middle
        if head is None or head.next is None:
            return

        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        first=head
        middle=slow.next
        slow.next=None
        second=self.reverse(middle)

        while second:
            first_next=first.next
            second_next=second.next

            first.next=second
            second.next=first_next

            first=first_next
            second=second_next
    
    def reverse(self,temp):
        curr=temp
        prev=None
        while curr:
            front=curr.next
            curr.next=prev
            prev=curr
            curr=front
        return prev
