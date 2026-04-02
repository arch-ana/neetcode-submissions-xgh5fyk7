# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        movingHead = None

        if head1 == head2 == None:
            return None
        elif head1 == None:
            return head2
        elif head2 == None:
            return head1
        else:
            if head1.val <= head2.val:
                movingHead = head1
                finalHead = movingHead
                head1 = head1.next
            else:
                movingHead = head2
                finalHead = movingHead
                head2 = head2.next
        
        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                movingHead.next = head1
                head1 = head1.next
            else:
                movingHead.next = head2
                head2 = head2.next
            movingHead = movingHead.next

        if head1 == None and head2 == None:
            return finalHead
        elif head1 == None:
            movingHead.next = head2
        else:
            movingHead.next = head1

        return finalHead

        