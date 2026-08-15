# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1, temp2 = list1, list2
        dummyNode = ListNode(-1)
        finalNode = dummyNode
        while (temp1 is not None) and (temp2 is not None):
            if temp1.val < temp2.val:
                finalNode.next = temp1
                finalNode = finalNode.next
                temp1 = temp1.next
            else:
                finalNode.next = temp2
                finalNode = finalNode.next
                temp2 = temp2.next
        
        while temp1:
            finalNode.next = temp1
            finalNode = finalNode.next
            temp1 = temp1.next
        
        while temp2:
            finalNode.next = temp2
            finalNode = finalNode.next
            temp2 = temp2.next

        return dummyNode.next
                