# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Base Case
        if head==None or head.next==None:
            return 

        length, temp1 = 0, head
        while temp1!=None:
            length +=1
            temp1 = temp1.next
        prev, temp = head, head
        nextNode = temp
        k = (abs(length - n))
        if k == 0:# Delete at first position
            return head.next 

        while k > 0:
            prev = temp
            temp = temp.next
            k-=1
        nextNode = temp.next
        prev.next = temp.next
        del(temp)
        return head
