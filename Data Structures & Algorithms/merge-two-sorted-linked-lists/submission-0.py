# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        mergedList = head

        while list1 != None or list2 != None:
            tempNode = None

            if list1 == None and list2 != None:
                tempNode = list2
                list2 = list2.next
            elif list1 != None and list2 == None:
                tempNode = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                tempNode = list1
                list1 = list1.next
            else:
                tempNode = list2
                list2 = list2.next

            mergedList.next = tempNode
            mergedList = mergedList.next

        return head.next