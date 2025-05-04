class Node:
    def __init__(self, value, nxt=None) -> None:
        self.value = value
        self.nxt = nxt


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        new_node.nxt = self.head
        self.head = new_node
        return

    def pop(self):
        if not self.head:
            return

        return_value = self.head.value
        self.head = self.head.nxt
        return return_value
