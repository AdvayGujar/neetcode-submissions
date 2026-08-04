# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = []
        traverse = head

        while traverse is not None:
            temp.append(traverse)
            traverse = traverse.next

        left = 1
        right = len(temp) - 1
        switch = 1
        traverse = temp[0]

        while left <= right:
            if switch == 1:
                traverse.next = temp[right]
                traverse = traverse.next
                right -= 1
                switch = 0
            else:
                traverse.next = temp[left]
                traverse = traverse.next
                left += 1
                switch = 1

        traverse.next = None