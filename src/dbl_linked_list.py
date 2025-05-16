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
        self.__strict = strict
        self.__type = None

    def push(self, value):
        """
        A new node to the head of the list.
        """

        if not self.head:
            self.length += 1
            self.__type = type(value)
            first_node = DblNode(value)
            self.head = first_node
            self.tail = first_node
            return

        if self.__strict:
            if type(value) is not self.__type:
                print("Strict list cannot contain multiple types.")
                return False

        self.length += 1
        new_node = DblNode(value)
        new_node.nxt = self.head
        self.head.prev = new_node
        self.head = new_node
