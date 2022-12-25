# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current_node = ListNode(head.val, None)
        current = head

        while current.next is not None:
            current = current.next
            current_node = ListNode(current.val, current_node)

        return current_node
