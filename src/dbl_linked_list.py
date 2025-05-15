"""
Double Linked List.
"""

from linked_list import LinkedList, Node


class DblNode(Node):
    def __init__(self, value, nxt=None, prev=None) -> None:
        super().__init__(value, nxt)
        self.prev = prev


class DblList(LinkedList):
    def __init__(self, length=0, strict=False) -> None:
        super().__init__(length, strict)
