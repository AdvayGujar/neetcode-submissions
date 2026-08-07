# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        start = head
        carry = 0
        place = 0

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                add = l1.val + l2.val + carry
                carry = add // 10
                add = add % 10

                newNode = ListNode(add)
                head.next = newNode
                head = head.next

                l1 = l1.next
                l2 = l2.next
            elif l1 is None and l2 is not None:
                add = l2.val + carry
                carry = add // 10
                add = add % 10

                newNode = ListNode(add)
                head.next = newNode
                head = head.next

                l2 = l2.next
            elif l1 is not None and l2 is None:
                add = l1.val + carry
                carry = add // 10
                add = add % 10

                newNode = ListNode(add)
                head.next = newNode
                head = head.next

                l1 = l1.next

        if carry > 0:
            newNode = ListNode(carry)
            head.next = newNode

        return start.next