"""
Queue.
"""


class Node:
    def __init__(self, value, nxt=None, prev=None) -> None:
        self.value = value
        self.nxt = nxt
        self.prev = prev


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        """
        Add a node to the tail of the queue.
        """

        self.length += 1
        node = Node(value)
        if not self.tail:
            self.tail = node
            self.head = node
            return

        node = Node(value)
        node.prev = self.tail
        self.tail.nxt = node
        self.tail = node
