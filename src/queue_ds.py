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
        return

    def dequeue(self):
        """
        Dequeue value from head of queue.
        """
        if not self.head:
            return

        self.length -= 1
        ret_val = self.head.value
        if not self.head.nxt:
            self.head = None
            self.tail = None
            return ret_val

        self.head = self.head.nxt
        return ret_val

    def peek(self):
        """
        Peek the value of the head node.
        """
        if not self.head:
            return
        return self.head.value
