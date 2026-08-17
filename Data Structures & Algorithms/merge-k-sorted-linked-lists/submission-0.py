# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        start = head

        while len(lists) != 0:
            minNode = lists[0]
            index = 0
            exitLoop = False

            for x in range(len(lists)):
                if lists[x] is not None:
                    if minNode.val > lists[x].val:
                        minNode = lists[x]
                        index = x
                else:
                    lists.pop(x)
                    exitLoop = True
                    break

            if exitLoop == False:
                head.next = minNode
                head = head.next

                if lists[index].next == None:
                    lists.pop(index)
                else:
                    lists[index] = lists[index].next

        return start.next