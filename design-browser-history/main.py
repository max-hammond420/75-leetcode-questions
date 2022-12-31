class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.current = self.homepage

    def visit(self, url: str) -> None:
        self.current.next = Node(url, self.current)
        self.current = self.current.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current.prev is not None:
                self.current = self.current.prev
            else:
                return self.current.value

        return self.current.value

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current.next is not None:
                self.current = self.current.next
            else:
                return self.current.value

        return self.current.value


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
