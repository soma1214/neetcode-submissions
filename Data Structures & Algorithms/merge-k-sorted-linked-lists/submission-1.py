# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """result=[]
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
        """
        if not lists:
            return None

        interval=1
        n=len(lists)
        while interval<n:
            for i in range(0,n-interval,interval*2):
                lists[i]=self.merge2lists(lists[i],lists[i+interval])
        
            interval*=2
        
        return lists[0]

    def merge2lists(self,l1,l2):
        dummy=ListNode(0)
        temp=dummy
        while l1 and l2:
            if l1.val<=l2.val:
                temp.next=l1
                temp=l1
                l1=l1.next
            else:
                temp.next=l2
                temp=l2
                l2=l2.next
        if l1:
            temp.next=l1
        if l2:
            temp.next=l2
        
        return dummy.next