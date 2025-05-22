import pytest

from queue import Queue, Node


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


class TestQueueClassHead:
    def test_Queue_initiates_with_head_attribute(self):
        """A Queue initializes with the .head attribute."""
        lst = Queue()
        assert hasattr(lst, "head")

    def test_Queue_initiates_with_head_as_None(self):
        """A Queue initializes with the .head attribute."""
        lst = Queue()
        assert not lst.head

    def test_Queue_initiates_with_tail_as_None(self):
        """A Queue initializes with the .tail attribute."""
        lst = Queue()
        assert not lst.tail

    def test_Queue_initiates_with_length_0(self):
        """A Queue initializes with the .length attribute."""
        lst = Queue()
        assert lst.length == 0
