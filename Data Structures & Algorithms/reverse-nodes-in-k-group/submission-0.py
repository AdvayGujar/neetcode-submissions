# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, start, end):
        reverse = None
        prevNode = None

        while start != end:
            n = start.next

            reverse = start
            reverse.next = prevNode
            prevNode = reverse

            start = n

        n = start.next

        reverse = start
        reverse.next = prevNode
        prevNode = reverse

        start = n

        return reverse

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        oneBeforeStart, oneAfterEnd = ListNode(None) , ListNode(0)
        oneBeforeStart.next = head
        start = ListNode(0)
        length = 1

        while head is not None:
            oneAfterEnd = head.next
            
            if length == k:
                self.reverse(oneBeforeStart.next, head)
                if oneBeforeStart.val is not None:
                    newOBS = oneBeforeStart.next
                    newOBS.next = oneAfterEnd
                    oneBeforeStart.next = head

                    oneBeforeStart = newOBS
                    head = oneAfterEnd

                else:
                    start.next = head
                    newOBS = oneBeforeStart.next
                    newOBS.next = oneAfterEnd

                    oneBeforeStart = newOBS
                    head = oneAfterEnd

                length = 1
            else:
                length += 1
                head = head.next

        return start.next