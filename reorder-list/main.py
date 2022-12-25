# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        current = head

        arr = []
        while current is not None:
            arr.append(current)
            current = current.next

        nodes = []
        for i in range(len(arr)//2):
            nodes.append(arr[i])
            nodes.append(arr[-i-1])

        if len(arr) % 2 != 0:
            nodes.append(arr[len(arr)//2])

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        nodes[-1].next = None

        return nodes[0]
