"""
Queue.
"""


class Node:
    def __init__(self, value, nxt=None) -> None:
        self.value = value
        self.nxt = nxt


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
