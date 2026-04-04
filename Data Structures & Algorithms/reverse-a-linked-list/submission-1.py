# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        iter1 = head
        iter2 = iter1.next
        iter3 = iter2.next

        iter2.next = iter1
        iter1.next = None

        while iter3:
            iter1 = iter2
            iter2 = iter3
            iter3 = iter3.next

            iter2.next = iter1

        return iter2

