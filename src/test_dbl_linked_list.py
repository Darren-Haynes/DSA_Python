import pytest

from dbl_linked_list import DblList, DblNode


class TestNode:
    def test_node_initiates_with_data_attribute(self):
        """A node object initializes with the 'value' attribute."""
        n = DblNode(1)
        assert hasattr(n, "value")

    def test_node_initiates_with_nxt_attribute(self):
        """A node object initializes with the 'nxt' attribute."""
        n = DblNode(1)
        assert hasattr(n, "nxt")

    def test_node_data_is_correct(self):
        """A node should initiate with the data passed into it's class."""
        n = DblNode(1)
        assert n.value == 1

    def test_TypeError_raised_node_no_data(self):
        """TypeError should raise when a value is not passed to DblNode class."""
        with pytest.raises(TypeError):
            DblNode()

    def test_node_nxt_value_is_None(self):
        """A node should initiate with it's .nxt attribute as None."""
        n = DblNode(1)
        assert not n.nxt


class TestDblListClassHead:
    def test_DblList_initiates_with_head_attribute(self):
        """A DblList initializes with the .head attribute."""
        lst = DblList()
        assert hasattr(lst, "head")

    def test_DblList_initiates_with_head_as_None(self):
        """A DblList initializes with the .head attribute."""
        lst = DblList()
        assert not lst.head

    def test_DblList_initiates_with_tail_as_None(self):
        """A DblList initializes with the .tail attribute."""
        lst = DblList()
        assert not lst.tail

    def test_DblList_initiates_with_length_0(self):
        """A DblList initializes with the .length attribute."""
        lst = DblList()
        assert lst.length == 0

    def test_DblList_initiates_with_type_None(self):
        """A DblList initializes with type as None."""
        lst = DblList()
        assert not lst._LinkedList__type

    def test_DblList_initiates_with_strict_False_as_default(self):
        """A DblList initializes with __stict as False."""
        lst = DblList()
        assert not lst._LinkedList__strict

    def test_DblList_initiates_with_strict_True(self):
        """A DblList initializes with __stict as True passed as kw arg."""
        lst = DblList(strict=True)
        assert lst._LinkedList__strict
