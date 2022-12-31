class MyLinkedList:

    def __init__(self):
        pass

    def get(self, index: int) -> int:
        local_current = self.head
        for _ in range(index):
            if local_current.next is None:
                return local_current.value
            else:
                local_current = local_current.next

        return local_current.value

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        self.head = new

    def addAtTail(self, val: int) -> None:
        local_current = self.head
        while local_current.next is not None:
            local_current = local_current.next

        local_current.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        local_current = self.head
        for i in range(1, index):
            if local_current.next is not None:
                if (i - 1) == index:
                    new_node = Node(val, local_current.next)
                    local_current.next = new_node
                    break
                local_current = local_current.next
            else:
                break

    def deleteAtIndex(self, index: int) -> None:
        local_current = self.head
        for i in range(1, index):
            if local_current.next is not None:
                if (i - 1) == index:
                    local_current.next = local_current.next.next
            else:
                break


class Node:

    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
