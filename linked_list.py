"""
Linked List.
"""


class Node:
    """
    Nodes to be used within a linked list.
    value: node must be instantiated with a value (data)
    nxt: instantiated as None.
    """

    def __init__(self, value, nxt=None) -> None:
        self.value = value
        self.nxt = nxt


class LinkedList:
    """
    A LINKED LIST.
    In addition to the standard push and pop methods that we associate with a
    LinkedList 'append' and 'pop_right' methods are implemented to access the
    other end of the list. Note that even though we have direct access to the
    end of the list, there are no backwards pointers i.e you can only iterate
    from head to tail. Thus this is not a doubly linked list.
    """

    def __init__(self, length=0, strict=False) -> None:
        """
        List instantiates with head and tail of 'None and length of 0"
        """
        self.head = None
        self.tail = None
        self.length = length
        self.__strict = strict
        self.__type = None

    def __str__(self):
        """
        Print the vaules of all the nodes in the list.
        """
        lst_content = "["
        current = self.head
        while current:
            lst_content = lst_content + str(current.value) + ", "
            current = current.nxt
        lst_content = lst_content.rstrip(", ")
        return lst_content + "]"

    def __repr__(self):
        """
        Print the vaules of all the nodes in the list.
        """
        return self.__str__()

    def __len__(self):
        # Custom special len method.
        """
        Returns the number of nodes in the list.
        """
        return self.length

    def push(self, value):
        """
        A new node to the head of the list.
        value: must be passed and can be any data type.
        """

        if not self.head:
            self.length += 1
            self.__type = type(value)
            first_node = Node(value)
            self.head = first_node
            self.tail = first_node
            return

        if self.__strict:
            if type(value) is not self.__type:
                print("Strict list cannot contain multiple types.")
                return False

        self.length += 1
        new_node = Node(value)
        new_node.nxt = self.head
        self.head = new_node
        return

    def pop(self):
        """
        Pops the head node and returns it's value.
        Takes no parameters.
        """
        if not self.head:
            return

        return_value = self.head.value
        self.head = self.head.nxt
        if not self.head:
            self.tail = None
        self.length -= 1
        return return_value

    def is_empty(self):
        """
        Check if the list has nodes.
        """
        if not self.head:
            return True
        return False

    def append(self, value):
        """
        Add a node to the end of the list.
        value: must be supplied and supports any data type.
        """
        if not self.head:
            self.__type = type(value)
            first_node = Node(value)
            self.head = first_node
            self.tail = first_node
            self.length += 1
            return first_node.value

        if self.__strict:
            if type(value) is not self.__type:
                print("Strict list cannot contain multiple types.")
                return False

        new_node = Node(value)
        self.tail.nxt = new_node
        self.tail = new_node
        self.length += 1
        return new_node.value

    def pop_right(self):
        """
        Pop the node at the tail end of the list.
        Takes no parameters.
        """
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
        """
        Removes all nodes from the list.
        Resets 'head' and 'tail' to None and length to 0.
        """
        self.head = None
        self.length = 0
        self.tail = 0
        return

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
        previous = self.head
        while current:
            if current.value == value:
                if self.tail == current:
                    self.tail = previous
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
        """
        Prints the contents of the list.
        Values of 10 nodes printed per line by default.
        'per_line' parameter can be change to overide default.
        """
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

    def _average(self, current):
        if not current:
            return 0
        return self._average(current.nxt) + current.value

    def average(self):
        """
        Returns the average of all the values in the list.
        """
        if not self.head:
            return 0
        total = self._average(self.head)
        if total:
            return total / self.length
        return total
