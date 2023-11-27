class Queue:

    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item: int) -> None:
        self.items.append(item)

    def dequeue(self) -> int:
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from an empty queue")

    def is_empty(self) -> bool:
        return not bool(self.items)

    def sort(self) -> None:
        self.items.sort()

    def to_stack(self) -> 'Stack':
        stack = Stack()
        for item in self.items:
            stack.push(item)
        return stack

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

def test_queue() -> None:
    queue = Queue()
    queue.enqueue(42)
    queue.enqueue(10)
    queue.enqueue(5)
    assert not queue.is_empty()
    assert queue.dequeue() == 42

    queue.sort()

    stack = queue.to_stack()
    assert stack.pop() == 10
    assert queue.dequeue() == 5

# Run the test
test_queue()
