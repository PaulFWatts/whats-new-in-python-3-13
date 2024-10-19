# queue312.py
from collections import deque

class Queue312[T]:
    def __init__(self) -> None:
        self.elements: deque[T] = deque()

    def push(self, element: T) -> None:
        self.elements.append(element)

    def pop(self) -> T:
        return self.elements.popleft()

queue = Queue312[int]()  # Must provide Type
queue.push(3)
queue.push("twelve")     # Typing error: must be an int
