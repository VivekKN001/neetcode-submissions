# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummyNode = ListNode(-1)
        reversed_list = dummyNode.next
        temp, height = head, 0

        # Base Condition
        if (head is None) or (head.next is None):
            return

        # Finding middle of Linked List
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        prev.next = None
        # Reversing and storing in reversed_list
        nextNode, temp1 = slow, slow
        while nextNode != None:
            nextNode = nextNode.next
            temp1.next = reversed_list
            reversed_list = temp1
            temp1 = nextNode
        
        # Reordering the List
        firstPointer, secondPointer = head, reversed_list
        while secondPointer and firstPointer:
            temp1 = firstPointer.next
            temp2 = secondPointer.next

            firstPointer.next = secondPointer
            secondPointer.next = temp1

            firstPointer = temp1
            secondPointer = temp2
        
        if secondPointer:
            tail = head
            while tail.next:
                tail = tail.next
            tail.next = secondPointer



        
