# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
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
        return 
