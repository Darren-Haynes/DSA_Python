class Node:
    def __init__(self, value, nxt=None) -> None:
        self.value = value
        self.nxt = nxt


class LinkedList:
    def __init__(self, length=0) -> None:
        self.head = None
        self.length = length

    def __str__(self):
        # Print the linked list contents
        lst_content = "["
        current = self.head
        while current:
            lst_content = lst_content + str(current.value) + ", "
            current = current.nxt
        lst_content = lst_content.rstrip(", ")
        return lst_content + "]"

    def __repr__(self):
        # Both __repr__ & __str__ return complete list
        return self.__str__()

    def __len__(self):
        # Custom special len method.
        return self.length

    def push(self, value):
        new_node = Node(value)
        self.length += 1
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
        self.length -= 1
        return return_value

    def is_empty(self):
        if not self.head:
            return True
        return False

    def _append(self, new_node, current):
        if not current.nxt:
            current.nxt = new_node
            return new_node
        current = current.nxt
        return self._append(new_node, current)

    def append(self, value):
        self.length += 1
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return new_node

        return self._append(new_node, self.head)

    def pop_right(self):
        if not self.head:
            return
        if not self.head.nxt:
            return_value = self.head.value
            self.head = None
            self.length -= 1
            return return_value

        previous = self.head
        current = self.head.nxt
        while current.nxt:
            previous = current
            current = current.nxt
        previous.nxt = None
        self.length -= 1
        return current.value

    def clear(self):
        self.head = None
        self.length = 0
        return

    def _delete(self, previous, current, value):
        if not current:
            return

        if current.value == value:
            return_node = current
            previous.nxt = current.nxt
            self.length -= 1
            return return_node

        return self._delete(previous.nxt, current.nxt, value)

    def delete(self, value):
        if not self.head:
            return

        if self.head.value == value:
            return_node = self.head
            self.head = self.head.nxt
            self.length -= 1
            return return_node

        return self._delete(self.head, self.head.nxt, value)

    def line_print(self, per_line=10):
        if not self.head:
            print("[]")
            return "[]"

        print("[ ")
        count = -1

        print_string = ""
        current = self.head
        while current:
            count += 1
            if count == per_line:
                count = 0
                print(print_string)
                print_string = ""

            print_string = print_string + str(current.value) + ", "
            current = current.nxt

        print(print_string)
        print("]\n")
        return self.__str__()
