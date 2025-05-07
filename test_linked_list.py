import pytest

from linked_list import LinkedList, Node
import linked_list


@pytest.fixture
def one_node():
    lst = LinkedList()
    lst.push(1)
    return lst


@pytest.fixture
def lst_factory(request):
    marker = request.node.get_closest_marker("lst_factory_data")

    # Do something with the data
    lst = LinkedList()
    for value in marker.args[0]:
        lst.push(value)
    return lst


class TestNode:
    def test_node_initiates_with_data_attribute(self):
        """A node object initializes with the 'value' attribute."""
        n = Node(1)
        assert hasattr(n, "value")

    def test_node_initiates_with_nxt_attribute(self):
        """A node object initializes with the 'nxt' attribute."""
        n = Node(1)
        assert hasattr(n, "nxt")

    def test_node_data_is_correct(self):
        """A node should initiate with the data passed into it's class."""
        n = Node(1)
        assert n.value == 1

    def test_TypeError_raised_node_no_data(self):
        """TypeError should raise when a value is not passed to Node class."""
        with pytest.raises(TypeError):
            Node()

    def test_node_nxt_value_is_None(self):
        """A node should initiate with it's .nxt attribute as None."""
        n = Node(1)
        assert not n.nxt


class TestLinkedListClassHead:
    def test_LinkedList_initiates_with_head_attribute(self):
        """A LinkedList initializes with the .head attribute."""
        lst = LinkedList()
        assert hasattr(lst, "head")

    def test_LinkedList_initiates_with_head_as_None(self):
        """A LinkedList initializes with the .head attribute."""
        lst = LinkedList()
        assert not lst.head


class TestPushMethod:
    def test_LinkedList_with_1_node_is_head(self, one_node):
        """Push 1 value into Linked List, that value should be the head's data"""
        assert one_node.head.value == 1

    def test_LinkedList_with_1_node_head_nxt_is_none(self, one_node):
        """Push 1 value into Linked List, head.nxt should be None"""
        assert not one_node.head.nxt

    @pytest.mark.lst_factory_data([1, 2])
    def test_LinkedList_with_2_nodes_correct_head(self, lst_factory):
        """Push 2 values into Linked List, last value pushed should be the head's data"""
        assert lst_factory.head.value == 2

    @pytest.mark.lst_factory_data([1, 2])
    def test_LinkedList_with_2_nodes_correct_head_nxt_data(self, lst_factory):
        """Push 2 values into Linked List, first value pushed should be head.nxt.data"""
        assert lst_factory.head.nxt.value == 1

    @pytest.mark.lst_factory_data([1, 2])
    def test_LinkedList_with_2_nodes_no_3rd_node(self, lst_factory):
        """Push 2 values into Linked List, there should be no 3rd node"""
        assert not lst_factory.head.nxt.nxt


class TestPopMethod:
    def test_pop_empty_head_returns_none(self):
        """If linked list is empty, popping head returns None."""
        lst = LinkedList()
        assert not lst.pop()

    def test_pop_list_with_1_node_returns_correct_value(self, one_node):
        """If lst has just one node, that value should be popped"""
        assert one_node.pop() == 1

    def test_pop_list_with_1_node_creates_empty_list(self, one_node):
        """A list with a single node should be empty after pop method"""
        one_node.pop()
        assert not one_node.head

    @pytest.mark.lst_factory_data([1, 2])
    def test_head_value_after_pop_list_with_2_nodes(self, lst_factory):
        """Pop list with 2 nodes, head's value should be first node pushed"""
        lst_factory.pop()
        assert lst_factory.head.value == 1

    @pytest.mark.lst_factory_data([1, 2])
    def test_head_nxt_after_pop_list_with_2_nodes(self, lst_factory):
        """Pop list with 2 nodes, head's nxt should be None."""
        lst_factory.pop()
        assert not lst_factory.head.nxt

    @pytest.mark.lst_factory_data([1, 2])
    def test_list_is_empty_after_popping_twice(self, lst_factory):
        """Pop twice list with 2 nodes, head should be None."""
        lst_factory.pop()
        lst_factory.pop()
        assert not lst_factory.head


class TestIsEmptyMethod:
    def test_freshly_initialized_list_is_empty(self):
        """A freshly coined list that has no nodes should be empty."""
        lst = LinkedList()
        assert lst.is_empty()

    def test_one_node_added_not_empty(self, one_node):
        """A freshly coined list that has no nodes should be empty."""
        assert not one_node.is_empty()

    def test_one_node_added_and_popped(self, one_node):
        """A list that has one node added and removed should be empty."""
        one_node.pop()
        assert one_node.is_empty()

    @pytest.mark.lst_factory_data([i for i in range(1, 11)])
    def test_add_and_pop_ten_nodes_empty(self, lst_factory):
        for _ in range(10):
            lst_factory.pop()
        assert lst_factory.is_empty()


class TestAppendMethod:
    def test_append_one_node_correct_head_value(self):
        """If list empty, head should become the value."""
        lst = LinkedList()
        lst.append(1)
        assert lst.head.value == 1

    def test_append_two_nodes_correct_head_value(self):
        """When append 2 nodes, the the first appended should be the head"""
        lst = LinkedList()
        lst.append(1)
        lst.append(2)
        assert lst.head.value == 1

    def test_append_two_nodes_correct_head_correct_nxt_value(self):
        """When append 2 nodes, the the second appended should be head.nxt's value"""
        lst = LinkedList()
        lst.append(1)
        lst.append(2)
        assert lst.head.nxt.value == 2

    def test_append_three_nodes_correct_third_node_value(self):
        """When append 3 nodes, last node appended has corrent value.
        This is to test recusive function calls itself."""
        lst = LinkedList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        assert lst.head.nxt.nxt.value == 3

    def test_append_three_nodes_correct_third_node_nxt(self):
        """When append 3 nodes, last node appended next is None"""
        lst = LinkedList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        assert not lst.head.nxt.nxt.nxt


class TestPopRightMethod:
    def test_pop_right_empty_list(self):
        """Empty list should return None."""
        lst = LinkedList()
        assert not lst.pop_right()

    def test_pop_right_with_one_node_return_value(self, one_node):
        """A list with single node should return nodes value"""
        assert one_node.pop_right() == 1

    def test_pop_right_with_one_node_creates_empty_list(self, one_node):
        """A list with sinlge node that gets popped should be empty."""
        one_node.pop_right()
        assert not one_node.head

    @pytest.mark.lst_factory_data([1, 2])
    def test_pop_right_with_two_nodes_returns_correct_value(self, lst_factory):
        """Right pop list with 2 nodes, first node pushed value should return."""
        assert lst_factory.pop_right() == 1

    @pytest.mark.lst_factory_data([1, 2, 3])
    def test_pop_right_with_three_nodes_returns_correct_value(self, lst_factory):
        """Right pop list with 3 nodes, first node pushed value should return."""
        assert lst_factory.pop_right() == 1

    @pytest.mark.lst_factory_data([1, 2])
    def test_head_nxt_after_pop_list_with_2_nodes(self, lst_factory):
        """Pop list with 2 nodes, head's nxt should be None."""
        lst_factory.pop()
        assert not lst_factory.head.nxt

    @pytest.mark.lst_factory_data([1, 2])
    def test_list_is_empty_after_popping_twice(self, lst_factory):
        """Pop twice list with 2 nodes, head should be None."""
        lst_factory.pop()
        lst_factory.pop()
        assert not lst_factory.head


class TestClearMethod:
    def test_clear_with_already_empty_list(self):
        """Already empty list returns none."""
        lst = LinkedList()
        assert not lst.clear()

    def test_clear_method_with_single_node(self, one_node):
        """Already empty list returns none."""
        assert not one_node.clear()

    @pytest.mark.lst_factory_data([i for i in range(1, 11)])
    def test_clear_method_with_ten_nodes(self, lst_factory):
        """Lst with 10 nodes should return None when cleared."""
        assert not lst_factory.clear()


class TestDeleteMethod:
    def test_delete_with_empty_list(self):
        """Empty list should return None."""
        lst = LinkedList()
        assert not lst.delete(1)

    def test_delete_with_single_node_no_match(self, one_node):
        """List with single non matching node value should return None"""
        assert not one_node.delete(2)

    def test_delete_with_single_node_match(self, one_node):
        """List with single matching node value should return matching Node"""
        match_node = one_node.head
        assert one_node.delete(1) == match_node

    def test_delete_with_single_node_match_returns_value(self, one_node):
        """List with single matching node value should return node with correct value."""
        match_node = one_node.delete(1)
        assert match_node.value == 1

    def test_delete_with_single_node_match_creates_empty_list(self, one_node):
        """List with single matching node value should return node with correct value."""
        one_node.delete(1)
        assert not one_node.head

    @pytest.mark.lst_factory_data([1, 2])
    def test_delete_with_2_nodes_no_match(self, lst_factory):
        """List with 2 non matching nodes should return none"""
        assert not lst_factory.delete(3)

    @pytest.mark.lst_factory_data([1, 2])
    def test_delete_with_2_nodes_head_matches(self, lst_factory):
        """List with single matching node value should return matching Node"""
        match_node = lst_factory.head
        assert lst_factory.delete(2) == match_node

    @pytest.mark.lst_factory_data([1, 2])
    def test_delete_with_2_nodes_returns_correct_value_of_head(self, lst_factory):
        """List with single matching node value should return node with correct value."""
        match_node = lst_factory.delete(2)
        assert match_node.value == 2


class TestSpecialMethodstr:
    def test_str_when_list_empty(self):
        """__str__ should return empty list string."""
        ll = LinkedList()
        assert ll.__str__() == "[]"

    def test_str_when_one_item_in_list(self, one_node):
        """__str__ should return list string with single item."""
        assert one_node.__str__() == "[1]"

    @pytest.mark.lst_factory_data([1, 2])
    def test_str_when_2_items_in_list(self, lst_factory):
        """__str__ should return list string with 2 items."""
        assert lst_factory.__str__() == "[2, 1]"

    @pytest.mark.lst_factory_data([1, 2, 3, 4, 5])
    def test_str_when_5_items_in_list(self, lst_factory):
        """__str__ should return list string with 5 items."""
        assert lst_factory.__str__() == "[5, 4, 3, 2, 1]"

    @pytest.mark.lst_factory_data([i for i in range(1, 101)])
    def test_str_when_100_items_in_list(self, lst_factory):
        """__str__ should return list string with 100 items."""
        python_lst = [i for i in range(100, 0, -1)]
        assert lst_factory.__str__() == python_lst.__str__()


class TestLinePrintMethod:
    def test_line_print_empty_list(self):
        """Empty list should return empty list string."""
        ll = LinkedList()
        assert ll.line_print() == "[]"

    @pytest.mark.lst_factory_data([1, 2, 3, 4, 5])
    def test_line_print_5_items(self, lst_factory):
        """5 item list should return __str__."""
        assert lst_factory.line_print() == "[5, 4, 3, 2, 1]"

    @pytest.mark.lst_factory_data([i for i in range(1, 12)])
    def test_line_print_11_items(self, lst_factory):
        """Test argument per_line"""
        python_lst = [i for i in range(11, 0, -1)]
        assert lst_factory.line_print() == python_lst.__str__()
