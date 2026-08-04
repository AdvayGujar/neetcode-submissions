# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        items = set()
        index = 0

        while head is not None:
            if head in items:
                return True
            else:
                items.add(head)
                head = head.next
        
        return False