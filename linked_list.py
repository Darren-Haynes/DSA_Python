class Node:
    def __init__(self, value, nxt=None) -> None:
        self.value = value
        self.nxt = nxt


class LinkedList:
    def __init__(self, length=0) -> None:
        self.head = None
        self.tail = None
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
            self.tail = new_node
            return

        new_node.nxt = self.head
        self.head = new_node
        return

    def pop(self):
        if not self.head:
            return

        return_value = self.head.value
        self.head = self.head.nxt
        if not self.head:
            self.tail = None
        self.length -= 1
        return return_value

    def is_empty(self):
        if not self.head:
            return True
        return False

    def append(self, value):
        self.length += 1
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return new_node.value

        self.tail.nxt = new_node
        self.tail = new_node

        return new_node.value

    def pop_right(self):
        if not self.head:
            return
        if not self.head.nxt:
            return_value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return return_value

        previous = self.head
        current = self.head.nxt
        while current.nxt:
            previous = current
            current = current.nxt
        previous.nxt = None
        self.tail = previous
        self.length -= 1
        return current.value

    def clear(self):
        self.head = None
        self.length = 0
        return

    def delete(self, value, del_num=1, del_all=False):
        """
        Returns how many times the value was deleted from the list.
        'del_num' argument determines how many times a deletion will occur.
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
                return deleted
            if not del_all:
                if deleted == del_num:
                    return deleted

        # Once head stops matching, continue through list
        current = self.head.nxt
        previous = self.head
        while current:
            if current.value == value:
                previous.nxt = current.nxt
                deleted += 1
                self.length -= 1
                if not del_all:
                    if deleted == del_num:
                        return deleted
            current = current.nxt
            previous = previous.nxt

        return deleted

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
