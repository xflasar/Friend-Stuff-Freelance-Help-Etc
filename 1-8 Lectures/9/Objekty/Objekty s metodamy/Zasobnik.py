class Stack:

    def __init__(self) -> None:
        self.items = []

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> int:
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from an empty stack")

    def is_empty(self) -> bool:
        return not bool(self.items)

def test_stack() -> None:
    stack = Stack()
    stack.push(5)
    stack.push(10)
    assert stack.pop() == 10
    assert not stack.is_empty()
    assert stack.pop() == 5
    assert stack.is_empty()

# Run the test
test_stack()
