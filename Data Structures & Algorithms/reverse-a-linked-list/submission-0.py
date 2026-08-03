# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None
        prevNode = None

        while head is not None:
            n = head.next

            reverse = head
            reverse.next = prevNode
            prevNode = reverse

            head = n

        return reverse
        