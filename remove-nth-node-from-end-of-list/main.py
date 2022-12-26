# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ls = []

        current = head
        while current is not None:
            ls.append(current)
            current = current.next

        ls.pop(-n)

        for i in range(len(ls)-1):
            ls[i].next = ls[i+1]

        if len(ls) == 0:
            return None

        ls[-1].next = None

        return ls[0]
