# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def get_sum(head):
            os = ""
            current = head
            while current is not None:
                os += str(current.val)
                current = current.next
            return int(os[::-1])

        sum = str(get_sum(l1) + get_sum(l2))
        sum = list(sum[::-1])

        if len(sum) == 0:
            return None

        dummy = ListNode(0, None)
        tail = dummy

        for i in range(len(sum)):
            tail.next = ListNode(int(sum[i]), None)
            tail = tail.next

        return dummy.next
