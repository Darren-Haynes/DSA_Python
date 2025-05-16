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


class TestPushMethod:
    def test_DblLinkedList_with_1_node_is_head(self, dbl_one_node):
        """Push 1 value into DblList, that value should be the head's data"""
        assert dbl_one_node.head.value == 1

    def test_DblLinkedList_with_1_node_is_tail(self, dbl_one_node):
        """Push 1 value into DblList, that value should be the head's data"""
        assert dbl_one_node.tail.value == 1

    def test_DblLinkedList_with_1_node_head_nxt_is_none(self, dbl_one_node):
        """Push 1 value into DblList, head.nxt should be None"""
        assert not dbl_one_node.head.nxt

    def test_DblLinkedList_with_1_node_tail_nxt_is_none(self, dbl_one_node):
        """Push 1 value into DblList, head.nxt should be None"""
        assert not dbl_one_node.tail.nxt

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_DblLinkedList_with_2_nodes_correct_head(self, dbl_lst_factory):
        """2 values in DblList, last value pushed should be head's data"""
        assert dbl_lst_factory.head.value == 2

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_DblLinkedList_with_2_nodes_prev(self, dbl_lst_factory):
        """2 values in DblList, first node pushed prev is head"""
        assert dbl_lst_factory.head.nxt.prev == dbl_lst_factory.head

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_DblList_with_2_nodes_correct_head_nxt_data(self, dbl_lst_factory):
        """2 values in DblList, first value pushed should be head.nxt.data"""
        assert dbl_lst_factory.head.nxt.value == 1

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_DblLinkedList_with_2_nodes_correct_tail(self, dbl_lst_factory):
        """2 values in DblList, first value pushed should be tail's value."""
        assert dbl_lst_factory.tail.value == 1

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_DblLinkedList_with_2_nodes_no_3rd_node(self, dbl_lst_factory):
        """Push 2 values into DblList, there should be no 3rd node"""
        assert not dbl_lst_factory.head.nxt.nxt


class TestPopMethod:
    def test_pop_empty_head_returns_none(self):
        """If linked list is empty, popping head returns None."""
        lst = DblList()
        assert not lst.pop()

    def test_pop_list_with_1_node_returns_correct_value(self, dbl_one_node):
        """If lst has just one node, that value should be popped"""
        assert dbl_one_node.pop() == 1

    def test_pop_list_with_1_node_creates_empty_list(self, dbl_one_node):
        """A list with a single node should be empty after pop method"""
        dbl_one_node.pop()
        assert not dbl_one_node.head

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_head_value_after_pop_list_with_2_nodes(self, dbl_lst_factory):
        """Pop list with 2 nodes, head's value should be first node pushed"""
        dbl_lst_factory.pop()
        assert dbl_lst_factory.head.value == 1

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_head_nxt_after_pop_list_with_2_nodes(self, dbl_lst_factory):
        """Pop list with 2 nodes, head's nxt should be None."""
        dbl_lst_factory.pop()
        assert not dbl_lst_factory.head.nxt

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_list_is_empty_after_popping_twice(self, dbl_lst_factory):
        """Pop twice list with 2 nodes, head should be None."""
        dbl_lst_factory.pop()
        dbl_lst_factory.pop()
        assert not dbl_lst_factory.head


class TestPopMethod:
    def test_pop_empty_head_returns_none(self):
        """If linked list is empty, popping head returns None."""
        lst = DblList()
        assert not lst.pop()

    def test_pop_list_with_1_node_returns_correct_value(self, dbl_one_node):
        """If lst has just one node, that value should be popped"""
        assert dbl_one_node.pop() == 1

    def test_pop_list_with_1_node_creates_empty_list(self, dbl_one_node):
        """A list with a single node should be empty after pop method"""
        dbl_one_node.pop()
        assert not dbl_one_node.head

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_head_value_after_pop_list_with_2_nodes(self, dbl_lst_factory):
        """Pop list with 2 nodes, head's value should be first node pushed"""
        dbl_lst_factory.pop()
        assert dbl_lst_factory.head.value == 1

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_head_nxt_after_pop_list_with_2_nodes(self, dbl_lst_factory):
        """Pop list with 2 nodes, head's nxt should be None."""
        dbl_lst_factory.pop()
        assert not dbl_lst_factory.head.nxt

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_list_is_empty_after_popping_twice(self, dbl_lst_factory):
        """Pop twice list with 2 nodes, head should be None."""
        dbl_lst_factory.pop()
        dbl_lst_factory.pop()
        assert not dbl_lst_factory.head
