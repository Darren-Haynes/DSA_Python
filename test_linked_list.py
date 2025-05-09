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
        assert lst.delete(1) == 0

    def test_delete_with_single_node_no_match(self, one_node):
        """List with single non matching node value should return 0"""
        assert one_node.delete(2) == 0

    def test_delete_with_single_node_match(self, one_node):
        """List with single matching node value should return 1"""
        assert one_node.delete(1) == 1

    def test_delete_with_single_node_match_creates_empty_list(self, one_node):
        """List with single matching node value should return node with correct value."""
        one_node.delete(1)
        assert not one_node.head

    @pytest.mark.lst_factory_data([1, 2])
    def test_delete_with_2_nodes_no_match(self, lst_factory):
        """List with 2 non matching nodes should return 0"""
        assert lst_factory.delete(3) == 0

    @pytest.mark.lst_factory_data([1, 2])
    def test_delete_with_2_nodes_head_matches(self, lst_factory):
        """List with single matching node value should return 1"""
        assert lst_factory.delete(2) == 1

    @pytest.mark.lst_factory_data([1, 2])
    def test_delete_with_2_nodes_returns_correct_value_of_head(self, lst_factory):
        """List with single matching node value should have only head node."""
        lst_factory.delete(2)
        assert lst_factory.head.value == 1

    @pytest.mark.lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_no_match(self, lst_factory):
        """List with 3 non matching nodes should return 0"""
        assert lst_factory.delete(4) == 0

    @pytest.mark.lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_head_matches(self, lst_factory):
        """List with single matching node value should return 1"""
        assert lst_factory.delete(3) == 1

    @pytest.mark.lst_factory_data([1, 2, 3])
    def test_delete_head_with_3_nodes_returns_correct_value_of_head(self, lst_factory):
        """List with single matching node value should return node with correct value."""
        lst_factory.delete(3)
        assert lst_factory.head.value == 2

    @pytest.mark.lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_tail_matches(self, lst_factory):
        """List with single matching last node value should return matching Node"""
        lst_factory.delete(1)
        assert lst_factory.head.nxt.value == 2

    @pytest.mark.lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_tail_matches_remaining_nodes(self, lst_factory):
        """List with single matching last node value should contain that node"""
        lst_factory.delete(1)
        assert lst_factory.__str__() == "[3, 2]"

    @pytest.mark.lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_middle_node_returns_1(self, lst_factory):
        """List with single matching mid node value should return 1"""
        assert lst_factory.delete(2) == 1

    @pytest.mark.lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_mid_node_matches_remaining_nodes(self, lst_factory):
        """List with single matching mid node value should not have that node"""
        lst_factory.delete(2)
        assert lst_factory.__str__() == "[3, 1]"

    @pytest.mark.lst_factory_data([1, 2, 2])
    def test_delete_with_3_nodes_delete_head_twice(self, lst_factory):
        """Deleting head value creates a new head, test new head deletes also"""
        lst_factory.delete(2, del_num=2)
        assert lst_factory.__str__() == "[1]"

    @pytest.mark.lst_factory_data([1, 2, 2])
    def test_delete_with_3_nodes_delete_head_twice_returns_2(self, lst_factory):
        """Deleting head value twice in 3 node list returns 2."""
        assert lst_factory.delete(2, del_num=2) == 2

    @pytest.mark.lst_factory_data([2, 2, 2])
    def test_delete_with_3_nodes_delete_head_thrice_returns_3(self, lst_factory):
        """Deleting head value thrice in 3 node list returns 2."""
        assert lst_factory.delete(2, del_num=3) == 3

    @pytest.mark.lst_factory_data([2] * 10)
    def test_delete_with_10_nodes_delete_head_10_times_returns_10(self, lst_factory):
        """Deleting head value 10 times using del_all=true param."""
        assert lst_factory.delete(2, del_all=True) == 10

    @pytest.mark.lst_factory_data([2] * 10)
    def test_length_with_10_nodes_delete_head_10_times(self, lst_factory):
        """Deleting head value 10 times using del_all=true param."""
        lst_factory.delete(2, del_all=True)
        assert len(lst_factory) == 0

    @pytest.mark.lst_factory_data([2, 1, 2, 1, 2, 1, 2, 1, 2, 1])
    def test_delete_with_10_nodes_delete_all_even_indexes(self, lst_factory):
        """Deleting all even index that have value 2 with del_all=true param."""
        assert lst_factory.delete(2, del_all=True) == 5

    @pytest.mark.lst_factory_data([2, 1, 2, 1, 2, 1, 2, 1, 2, 1])
    def test_length_with_10_nodes_delete_all_even_indexes(self, lst_factory):
        """Deleting all even index that have value 2 with del_all=true param."""
        lst_factory.delete(2, del_all=True)
        assert len(lst_factory) == 5

    @pytest.mark.lst_factory_data([2, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    def test_delete_with_10_nodes_delete_all_nodes_but_head(self, lst_factory):
        """Deleting all even index that have value 2 with del_all=true param."""
        lst_factory.delete(1, del_num=9)
        assert lst_factory.__str__() == "[2]"

    def test_non_int_passed_as_param(self):
        """Delete should return 0 if 'del_num' param is not int."""
        ll = LinkedList()
        assert ll.delete(1, del_num=1.1) == 0

    def test_int_less_than_1_param(self):
        """Delete should return 0 if 'del_num' is less than 1."""
        ll = LinkedList()
        assert ll.delete(1, del_num=0) == 0

    def test_non_bool_passed_as_param(self):
        """Delete should return 0 if 'del_all' param is not bool."""
        ll = LinkedList()
        assert ll.delete(1, del_all=1) == 0


class TestSpecialMethodStrAndRepr:
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

    def test_repr_when_list_empty(self):
        """__str__ should return empty list string."""
        ll = LinkedList()
        assert ll.__repr__() == "[]"

    def test_repr_when_one_item_in_list(self, one_node):
        """__str__ should return list string with single item."""
        assert one_node.__repr__() == "[1]"


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


class TestLength:
    def test_correct_length_on_instantition(self):
        """When created a new list, length should be = 1."""
        ll = LinkedList()
        assert ll.length == 0

    @pytest.mark.parametrize("nodes,exp_len", [(i, i) for i in range(1, 11)])
    def test_push_10_nodes_creates_correct_lengths(self, nodes, exp_len):
        """Test list with 1-10 nodes via push method has correct length."""
        ll = LinkedList()
        for i in range(1, nodes + 1):
            ll.push(i)
        assert ll.length == exp_len

    @pytest.mark.parametrize("nodes,exp_len", [(i, i) for i in range(1, 11)])
    def test_append_10_nodes_creates_correct_lengths(self, nodes, exp_len):
        """Test list with 1-10 nodes via append method has correct length."""
        ll = LinkedList()
        for i in range(1, nodes + 1):
            ll.append(i)
        assert ll.length == exp_len

    @pytest.mark.parametrize("nodes,exp_len", [(i, 10 - i) for i in range(1, 11)])
    def test_pop_10_nodes_creates_correct_lengths(self, nodes, exp_len):
        """Test list with 10 nodes popped 1 at a time has correct length."""
        ll = LinkedList()
        for i in range(1, 11):
            ll.push(i)
        for i in range(1, nodes + 1):
            ll.pop()
        assert ll.length == exp_len

    @pytest.mark.parametrize("nodes,exp_len", [(i, 10 - i) for i in range(1, 11)])
    def test_delete_10_nodes_creates_correct_lengths(self, nodes, exp_len):
        """Test list with 1-10 nodes deleted has correct length."""
        ll = LinkedList()
        for i in range(1, 11):
            ll.push(i)
        for i in range(1, nodes + 1):
            ll.delete(i)
        assert ll.length == exp_len

    @pytest.mark.parametrize("nodes,exp_len", [(i, 0) for i in range(1, 11)])
    def test_clear_list_with_1_to_10_nodes(self, nodes, exp_len):
        """Test list with 1-10 nodes via append method has correct length."""
        ll = LinkedList()
        for i in range(1, 11):
            ll.push(i)
        ll.clear()
        assert ll.length == exp_len

    def test_correct_len_on_instantition(self):
        """When created a new list, len() should be = 1."""
        ll = LinkedList()
        assert len(ll) == 0

    @pytest.mark.parametrize("nodes,exp_len", [(i, i) for i in range(1, 11)])
    def test_push_10_nodes_creates_correct_len(self, nodes, exp_len):
        """Test list with 1-10 nodes via push method has correct length."""
        ll = LinkedList()
        for i in range(1, nodes + 1):
            ll.push(i)
        assert len(ll) == exp_len

    @pytest.mark.parametrize("nodes,exp_len", [(i, i) for i in range(1, 11)])
    def test_append_10_nodes_creates_correct_len(self, nodes, exp_len):
        """Test list with 1-10 nodes via append method has correct length."""
        ll = LinkedList()
        for i in range(1, nodes + 1):
            ll.append(i)
        assert len(ll) == exp_len

    @pytest.mark.parametrize("nodes,exp_len", [(i, 10 - i) for i in range(1, 11)])
    def test_pop_10_nodes_creates_correct_len(self, nodes, exp_len):
        """Test list with 10 nodes popped 1 at a time has correct length."""
        ll = LinkedList()
        for i in range(1, 11):
            ll.push(i)
        for i in range(1, nodes + 1):
            ll.pop()
        assert len(ll) == exp_len

    @pytest.mark.parametrize("nodes,exp_len", [(i, 10 - i) for i in range(1, 11)])
    def test_delete_10_nodes_creates_correct_len(self, nodes, exp_len):
        """Test list with 1-10 nodes deleted has correct length."""
        ll = LinkedList()
        for i in range(1, 11):
            ll.push(i)
        for i in range(1, nodes + 1):
            ll.delete(i)
        assert len(ll) == exp_len

    @pytest.mark.parametrize("nodes,exp_len", [(i, 0) for i in range(1, 11)])
    def test_clear_list_with_1_to_10_nodes_corrent_len(self, nodes, exp_len):
        """Test list with 1-10 nodes via append method has correct length."""
        ll = LinkedList()
        for i in range(1, 11):
            ll.push(i)
        ll.clear()
        assert len(ll) == exp_len


class TestTailWithPushAndPop:
    def test_empty_list_has_no_tail(self):
        """An freshly coined linked list should be empty and with a tail."""
        lst = LinkedList()
        assert not lst.tail

    def test_push_one_node_is_tail(self, one_node):
        """A list with a single pushed node, that node should be the tail."""
        assert one_node.tail.value == 1

    def test_push_one_node_is_tail_and_head(self, one_node):
        """A list with a single pushed node, node should be head and tail."""
        assert one_node.tail == one_node.head

    @pytest.mark.lst_factory_data([1, 2])
    def test_push_2_nodes_has_right_tail_value(self, lst_factory):
        """A list with two nodes, last node should be tail."""
        assert lst_factory.tail.value == 1

    @pytest.mark.lst_factory_data([1, 2, 3])
    def test_push_3_nodes_has_right_tail_value(self, lst_factory):
        """A list with 3 nodes, last node should be tail."""
        assert lst_factory.tail.value == 1

    def test_pop_lst_with_single_node_has_no_tail(self, one_node):
        """If popping only node in list then tail should be None."""
        one_node.pop()
        assert not one_node.tail

    @pytest.mark.lst_factory_data([1, 2])
    def test_2_nodes_pop_one_node_has_right_tail(self, lst_factory):
        """Pop 1 node from 2 node list, head and tail should be same node."""
        lst_factory.pop()
        assert lst_factory.tail == lst_factory.head

    @pytest.mark.lst_factory_data([1, 2, 3])
    def test_3_nodes_pop_one_node_has_right_tail(self, lst_factory):
        """Pop 1 node from 3 node list, head.nxt should nbe tail."""
        lst_factory.pop()
        assert lst_factory.tail == lst_factory.head.nxt
