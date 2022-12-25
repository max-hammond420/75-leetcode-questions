# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []

        current = head

        while current is not None:
            seen.append(current)
            if current.next in seen:
                return True
            current = current.next
        return False
