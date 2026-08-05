# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        index = []

        while temp is not None:
            index.append(temp)
            temp = temp.next

        if len(index) == 1:
            head = index.pop()
            head = head.next
            return head

        index.pop(-n)

        for x in range(0,len(index)):
            if x == 0:
                head = index[x]
                temp = index[x]
                continue

            temp.next = index[x]
            temp = temp.next

        temp.next = None

        return head