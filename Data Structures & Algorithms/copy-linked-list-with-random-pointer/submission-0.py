"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ogList = []

        while head is not None:
            ogList.append(head)
            head = head.next

        if not ogList:
            newNode = Node(0, None, None)
            return newNode.next

        newList = []

        for x in range(len(ogList)):
            newNode = Node(ogList[x].val, None, None)
            newList.append(newNode)

        for x in range(len(newList)):
            if x != len(newList) - 1:
                newList[x].next = newList[x+1]
                if ogList[x].random is not None:
                    newList[x].random = newList[ogList.index(ogList[x].random)]
            else:
                if ogList[x].random is not None:
                    newList[x].random = newList[ogList.index(ogList[x].random)]

        return newList[0]      