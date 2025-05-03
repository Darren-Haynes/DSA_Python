import pytest

from linked_list import LinkedList, Node


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
        """A node object initializes with the 'data' attribute."""
        n = Node(1)
        assert hasattr(n, "data")

    def test_node_initiates_with_nxt_attribute(self):
        """A node object initializes with the 'nxt' attribute."""
        n = Node(1)
        assert hasattr(n, "nxt")

    def test_node_data_is_correct(self):
        """A node should initiate with the data passed into it's class."""
        n = Node(1)
        assert n.data == 1

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
        assert one_node.head.data == 1

    def test_LinkedList_with_1_node_head_nxt_is_none(self, one_node):
        """Push 1 value into Linked List, head.nxt should be None"""
        assert not one_node.head.nxt

    @pytest.mark.lst_factory_data([1, 2])
    def test_LinkedList_with_2_nodes_correct_head(self, lst_factory):
        """Push 2 values into Linked List, last value pushed should be the head's data"""
        assert lst_factory.head.data == 2

    @pytest.mark.lst_factory_data([1, 2])
    def test_LinkedList_with_2_nodes_correct_head_nxt_data(self, lst_factory):
        """Push 2 values into Linked List, first value pushed should be head.nxt.data"""
        assert lst_factory.head.nxt.data == 1

    @pytest.mark.lst_factory_data([1, 2])
    def test_LinkedList_with_2_nodes_no_3rd_node(self, lst_factory):
        """Push 2 values into Linked List, there should be no 3rd node"""
        assert not lst_factory.head.nxt.nxt
