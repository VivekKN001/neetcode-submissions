# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1, temp2 = l1, l2
        dummyNode = ListNode(-1)
        finalNode = dummyNode
        total = 0
        carry = 0
        while temp1!=None or temp2!=None:
            total = carry
            if temp1:
                total += temp1.val
                temp1 = temp1.next
            if temp2:
                total += temp2.val
                temp2 = temp2.next

            carry = total//10

            newNode = ListNode(total%10)
            finalNode.next = newNode
            finalNode = finalNode.next
        
        if carry:
            newNode = ListNode(carry)
            finalNode.next = newNode
            finalNode = finalNode.next
        
        return dummyNode.next
       