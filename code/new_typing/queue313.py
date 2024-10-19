# queue313.py
from collections import deque

class Queue[T = int]:
    def __init__(self) -> None:
        self.elements: deque[T] = deque()

    def push(self, element: T) -> None:
        self.elements.append(element)

    def pop(self) -> T:
        return self.elements.popleft()

queue = Queue()  # Defaults to Queue[int]
queue.push(3)
queue.push("thirteen")   # Typing error, not an int
