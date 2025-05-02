class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.nxt = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
