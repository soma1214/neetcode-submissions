# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result=[]
        for head in lists:
            temp=head
            while temp:
                result.append(temp.val)
                temp=temp.next
        result.sort()
        dummy=ListNode(0)
        temp=dummy
        for val in result:
            temp.next=ListNode(val)
            temp=temp.next
        return dummy.next