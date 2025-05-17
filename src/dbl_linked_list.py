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
        self._strict = strict
        self._type = None

    def push(self, value):
        """
        A new node to the head of the list.
        """

        if not self.head:
            self.length += 1
            self._type = type(value)
            first_node = DblNode(value)
            self.head = first_node
            self.tail = first_node
            return

        if self._strict:
            if type(value) is not self._type:
                print("Strict list cannot contain multiple types.")
                return False

        self.length += 1
        new_node = DblNode(value)
        new_node.nxt = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, value):
        """
        Add a node to the end of the list.
        value: must be supplied and supports any data type.
        However values are restricted to a specific type with _strict
        """
        if not self.head:
            self._type = type(value)
            first_node = DblNode(value)
            self.head = first_node
            self.tail = first_node
            self.length += 1
            return first_node.value

        if self._strict:
            if type(value) is not self._type:
                print("Strict list cannot contain multiple types.")
                return False

        new_node = DblNode(value)
        self.tail.nxt = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def pop_right(self):
        """
        Pop the node at the tail end of the list.
        Takes no parameters.
        """
        if not self.tail:
            return

        return_value = self.tail.value

        if not self.tail.prev:
            self.tail = None
            self.head = None
            self.length -= 1
            return return_value

        self.tail = self.tail.prev
        self.tail.nxt = None
        return return_value

    def delete(self, value, del_num=1, del_all=False):
        """
        Returns how many times the value was deleted from the list.
        'del_num' parameter determines how many times a deletion will occur.
        'del_num=1' (the default) will delete the first found instance only.
        'del_all=True' will overide any value of 'del_num'
        """
        if type(del_num) is not int:
            print("'del_num' param must be an int")
            return 0

        if type(del_all) is not bool:
            print("'del_all' param must be a bool")
            return 0

        if del_num < 1:
            print("'del_num=' parameter must be an int greater than 0")
            return 0

        if not self.head:
            return 0

        deleted = 0
        # First keep checking if head matches
        while self.head.value == value:
            print(self.head.value)
            self.head = self.head.nxt
            deleted += 1
            self.length -= 1
            if not self.head:
                self.tail = None
                return deleted
            if not del_all:
                if deleted == del_num:
                    return deleted

        # Once head stops matching, continue through list
        current = self.head.nxt
        while current:
            if current.value == value:
                if self.tail == current:
                    self.tail = self.tail.prev
                    self.tail.nxt = None
                else:
                    current.nxt.prev = current.prev
                    current.prev.nxt = current.nxt
                deleted += 1
                self.length -= 1
                if not del_all:
                    if deleted == del_num:
                        return deleted
            current = current.nxt

        return deleted

    def _average(self, current):
        if not current:
            return 0
        return self._average(current.nxt) + current.value

    def average(self):
        super().average()
        """
        Returns the average of all the values in the list.
        """
        if not self._strict:
            print("Average function requires strict list.")
            return

        if self._type not in [int, float, complex]:
            print("Average function only supports numerical values.")
            return

        total = self._average(self.head)
        if total:
            return total / self.length
        return total
