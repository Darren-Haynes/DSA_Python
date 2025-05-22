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
        assert not lst._type

    def test_DblList_initiates_with_strict_False_as_default(self):
        """A DblList initializes with __stict as False."""
        lst = DblList()
        assert not lst._strict

    def test_DblList_initiates_with_strict_True(self):
        """A DblList initializes with __stict as True passed as kw arg."""
        lst = DblList(strict=True)
        assert lst._strict


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


class TestAppendMethod:
    def test_append_one_node_correct_head_value(self):
        """If list empty, head should become the value."""
        lst = DblList()
        lst.append(1)
        assert lst.head.value == 1

    def test_append_two_nodes_correct_head_value(self):
        """When append 2 nodes, the the first appended should be the head"""
        lst = DblList()
        lst.append(1)
        lst.append(2)
        assert lst.head.value == 1

    def test_append_two_nodes_correct_tail(self):
        """When append 2 nodes, the the 2nd appended should be the tail"""
        lst = DblList()
        lst.append(1)
        lst.append(2)
        assert lst.tail.value == 2

    def test_append_two_nodes_correct_tail_prev(self):
        """When append 2 nodes, the the 2nd appended should be the tail"""
        lst = DblList()
        lst.append(1)
        lst.append(2)
        assert lst.tail.prev == lst.head

    def test_append_two_nodes_correct_head_correct_nxt_value(self):
        """When append 2 nodes, the the second appended should be head.nxt's value"""
        lst = DblList()
        lst.append(1)
        lst.append(2)
        assert lst.head.nxt.value == 2

    def test_append_three_nodes_correct_third_node_value(self):
        """When append 3 nodes, last node appended has corrent value.
        This is to test recusive function calls itself."""
        lst = DblList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        assert lst.head.nxt.nxt.value == 3

    def test_append_three_nodes_correct_third_node_nxt(self):
        """When append 3 nodes, last node appended next is None"""
        lst = DblList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        assert not lst.head.nxt.nxt.nxt

    def test_append_three_nodes_correct_third_node_prev(self):
        """When append 3 nodes, last node appended has corrent value.
        This is to test recusive function calls itself."""
        lst = DblList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        assert lst.tail.prev.value == 2


class TestPopRightMethod:
    def test_pop_right_empty_list(self):
        """Empty list should return None."""
        lst = DblList()
        assert not lst.pop_right()

    def test_pop_right_with_one_node_return_value(self, dbl_one_node):
        """A list with single node should return nodes value"""
        assert dbl_one_node.pop_right() == 1

    def test_pop_right_with_one_node_creates_empty_list(self, dbl_one_node):
        """A list with sinlge node that gets popped should be empty."""
        dbl_one_node.pop_right()
        assert not dbl_one_node.head

    def test_pop_right_with_one_node_has_empty_tail(self, dbl_one_node):
        """A list with sinlge node that gets popped should be empty."""
        dbl_one_node.pop_right()
        assert not dbl_one_node.tail

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_pop_right_with_2_nodes_returns_correct_value(self, dbl_lst_factory):
        """Right pop list with 2 nodes, first node pushed value should return."""
        assert dbl_lst_factory.pop_right() == 1

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_pop_right_with_2_nodes_has_correct_tail(self, dbl_lst_factory):
        """Right pop list with 2 nodes, tail is right value."""
        dbl_lst_factory.pop_right()
        assert dbl_lst_factory.tail.value == 2

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_pop_right_with_2_nodes_tail_head_same(self, dbl_lst_factory):
        """Right pop list with 2 nodes, tail and head same node."""
        dbl_lst_factory.pop_right()
        assert dbl_lst_factory.tail is dbl_lst_factory.head

    @pytest.mark.dbl_lst_factory_data([1, 2, 3])
    def test_pop_right_with_three_nodes_returns_correct_value(self, dbl_lst_factory):
        """Right pop list with 3 nodes, first node pushed value should return."""
        assert dbl_lst_factory.pop_right() == 1

    @pytest.mark.dbl_lst_factory_data([1, 2, 3])
    def test_pop_right_with_three_nodes_tail_is_correct(self, dbl_lst_factory):
        """Right pop list with 3 nodes, tail has correct value."""
        dbl_lst_factory.pop_right()
        assert dbl_lst_factory.tail.value == 2

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


class TestTypeChecking:
    params = [(1, int), (1.1, float), (1j, complex), ("1", str)]

    @pytest.mark.parametrize("value,exp_type", params)
    def test_push_first_node_has_correct___type_attribute(self, value, exp_type):
        lst = DblList()
        lst.push(value)
        assert lst._type == exp_type

    params2 = [(1, 1.1), (1.1, 1), (1j, 1), ("1", 1)]

    @pytest.mark.parametrize("node1,node2", params2)
    def test_2nd_node_of_diff_type_returns_False(self, node1, node2):
        """Test 2nd node pushed with non-matching value when strict."""
        lst = DblList(strict=True)
        lst.push(node1)
        assert not lst.push(node2)

    @pytest.mark.parametrize("node1,node2", params2)
    def test_2nd_node_of_diff_type_allowed_when_not_strict(self, node1, node2):
        """Test 2nd node pushed with non-matching value when strict."""
        lst = DblList()
        lst.push(node1)
        lst.push(node2)
        assert lst.head.value == node2

    @pytest.mark.parametrize("value,exp_type", params)
    def test_append_first_node_has_correct___type_attribute(self, value, exp_type):
        lst = DblList()
        lst.append(value)
        assert lst._type == exp_type

    params2 = [(1, 1.1), (1.1, 1), (1j, 1), ("1", 1)]

    @pytest.mark.parametrize("node1,node2", params2)
    def test_2nd_node_of_diff_type_appended_returns_False(self, node1, node2):
        """Test 2nd node pushed with non-matching value when strict."""
        lst = DblList(strict=True)
        lst.append(node1)
        assert not lst.append(node2)

    @pytest.mark.parametrize("node1,node2", params2)
    def test_2nd_node_append_of_diff_type_allowed_when_not_strict(self, node1, node2):
        """Test 2nd node pushed with non-matching value when strict."""
        lst = DblList()
        lst.append(node1)
        lst.append(node2)
        assert lst.head.value == node1


class TestDeleteMethod:
    def test_delete_with_empty_list(self):
        """Empty list should return None."""
        lst = DblList()
        assert lst.delete(1) == 0

    def test_delete_with_single_node_no_match(self, dbl_one_node):
        """List with single non matching node value should return 0"""
        assert dbl_one_node.delete(2) == 0

    def test_delete_with_single_node_match(self, dbl_one_node):
        """List with single matching node value should return 1"""
        assert dbl_one_node.delete(1) == 1

    def test_delete_with_single_node_match_creates_empty_list(self, dbl_one_node):
        """List with single matching node value should return node with correct value."""
        dbl_one_node.delete(1)
        assert not dbl_one_node.head

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_delete_with_2_nodes_no_match(self, dbl_lst_factory):
        """List with 2 non matching nodes should return 0"""
        assert dbl_lst_factory.delete(3) == 0

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_delete_with_2_nodes_head_matches(self, dbl_lst_factory):
        """List with single matching node value should return 1"""
        assert dbl_lst_factory.delete(2) == 1

    @pytest.mark.dbl_lst_factory_data([1, 2])
    def test_delete_with_2_nodes_returns_correct_value_of_head(self, dbl_lst_factory):
        """List with single matching node value should have only head node."""
        dbl_lst_factory.delete(2)
        assert dbl_lst_factory.head.value == 1

    @pytest.mark.dbl_lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_no_match(self, dbl_lst_factory):
        """List with 3 non matching nodes should return 0"""
        assert dbl_lst_factory.delete(4) == 0

    @pytest.mark.dbl_lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_head_matches(self, dbl_lst_factory):
        """List with single matching node value should return 1"""
        assert dbl_lst_factory.delete(3) == 1

    @pytest.mark.dbl_lst_factory_data([1, 2, 3])
    def test_delete_head_with_3_nodes_returns_correct_value_of_head(
        self, dbl_lst_factory
    ):
        """List with single matching node value should return node with correct value."""
        dbl_lst_factory.delete(3)
        assert dbl_lst_factory.head.value == 2

    @pytest.mark.dbl_lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_tail_matches(self, dbl_lst_factory):
        """List with single matching last node value should return matching Node"""
        dbl_lst_factory.delete(1)
        assert dbl_lst_factory.head.nxt.value == 2

    @pytest.mark.dbl_lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_tail_matches_remaining_nodes(self, dbl_lst_factory):
        """List with single matching last node value should contain that node"""
        dbl_lst_factory.delete(1)
        assert dbl_lst_factory.__str__() == "[3, 2]"

    @pytest.mark.dbl_lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_middle_node_returns_1(self, dbl_lst_factory):
        """List with single matching mid node value should return 1"""
        assert dbl_lst_factory.delete(2) == 1

    @pytest.mark.dbl_lst_factory_data([1, 2, 3])
    def test_delete_with_3_nodes_mid_node_matches_remaining_nodes(
        self, dbl_lst_factory
    ):
        """List with single matching mid node value should not have that node"""
        dbl_lst_factory.delete(2)
        assert dbl_lst_factory.__str__() == "[3, 1]"

    @pytest.mark.dbl_lst_factory_data([1, 2, 2])
    def test_delete_with_3_nodes_delete_head_twice(self, dbl_lst_factory):
        """Deleting head value creates a new head, test new head deletes also"""
        dbl_lst_factory.delete(2, del_num=2)
        assert dbl_lst_factory.__str__() == "[1]"

    @pytest.mark.dbl_lst_factory_data([1, 2, 2])
    def test_delete_with_3_nodes_delete_head_twice_returns_2(self, dbl_lst_factory):
        """Deleting head value twice in 3 node list returns 2."""
        assert dbl_lst_factory.delete(2, del_num=2) == 2

    @pytest.mark.dbl_lst_factory_data([2, 2, 2])
    def test_delete_with_3_nodes_delete_head_thrice_returns_3(self, dbl_lst_factory):
        """Deleting head value thrice in 3 node list returns 2."""
        assert dbl_lst_factory.delete(2, del_num=3) == 3

    @pytest.mark.dbl_lst_factory_data([2] * 10)
    def test_delete_with_10_nodes_delete_head_10_times_returns_10(
        self, dbl_lst_factory
    ):
        """Deleting head value 10 times using del_all=true param."""
        assert dbl_lst_factory.delete(2, del_all=True) == 10

    @pytest.mark.dbl_lst_factory_data([2] * 10)
    def test_length_with_10_nodes_delete_head_10_times(self, dbl_lst_factory):
        """Deleting head value 10 times using del_all=true param."""
        dbl_lst_factory.delete(2, del_all=True)
        assert len(dbl_lst_factory) == 0

    @pytest.mark.dbl_lst_factory_data([2, 1, 2, 1, 2, 1, 2, 1, 2, 1])
    def test_delete_with_10_nodes_delete_all_even_indexes(self, dbl_lst_factory):
        """Deleting all even index that have value 2 with del_all=true param."""
        assert dbl_lst_factory.delete(2, del_all=True) == 5

    @pytest.mark.dbl_lst_factory_data([2, 1, 2, 1, 2, 1, 2, 1, 2, 1])
    def test_length_with_10_nodes_delete_all_even_indexes(self, dbl_lst_factory):
        """Deleting all even index that have value 2 with del_all=true param."""
        dbl_lst_factory.delete(2, del_all=True)
        assert len(dbl_lst_factory) == 5

    @pytest.mark.dbl_lst_factory_data([2, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    def test_delete_with_10_nodes_delete_all_nodes_but_head(self, dbl_lst_factory):
        """Deleting all even index that have value 2 with del_all=true param."""
        dbl_lst_factory.delete(1, del_num=9)
        assert dbl_lst_factory.__str__() == "[2]"

    def test_non_int_passed_as_param(self):
        """Delete should return 0 if 'del_num' param is not int."""
        ll = DblList()
        assert ll.delete(1, del_num=1.1) == 0

    def test_int_less_than_1_param(self):
        """Delete should return 0 if 'del_num' is less than 1."""
        ll = DblList()
        assert ll.delete(1, del_num=0) == 0

    def test_non_bool_passed_as_param(self):
        """Delete should return 0 if 'del_all' param is not bool."""
        ll = DblList()
        assert ll.delete(1, del_all=1) == 0


class TestAverageMethod:
    def test_list_strict_print_statement(self, capsys):
        """Strict list with non numerical value prints correct statement."""
        lst = DblList(strict=True)
        lst.push("1")
        lst.average()
        captured = capsys.readouterr()
        assert captured.out == "Average function only supports numerical values.\n"

    def test_list_wrong_type_print_statement(self, capsys):
        """Strict list with non numerical value prints correct statement."""
        lst = DblList(strict=True)
        lst.push("1")
        lst.average()
        captured = capsys.readouterr()
        assert captured.out == "Average function only supports numerical values.\n"

    def test_list_non_strict_list_print_statement(self, capsys):
        """Strict list with non numerical value prints correct statement."""
        lst = DblList()
        lst.push("1")
        lst.average()
        captured = capsys.readouterr()
        assert captured.out == "Average function requires strict list.\n"

    def test_list_of_right_type_no_head(self):
        """If strict and right type but empty list, return None."""
        lst = DblList(strict=True)
        assert not lst.average()

    def test_empty_list_returns_none(self):
        """An empty list should return."""
        lst = DblList(strict=True)
        assert not lst.average()

    def test_list_with_single_node_with_value_0(self):
        """If single node with value 0, 0 should be returned."""
        lst = DblList(strict=True)
        lst.push(0)
        assert lst.average() == 0

    @pytest.mark.lst_factory_data([0, 0])
    def test_list_with_2_nodes_both_with_values_0(self, strict_lst_factory):
        """If list has 2 nodes, eachwith value 0, 0 should be returned."""
        assert strict_lst_factory.average() == 0

    @pytest.mark.parametrize("value,avg", [(i, i) for i in range(1, 11)])
    def test_list_with_single_node_with_value(self, value, avg):
        """If single node with value > 0, that number should be returned."""
        lst = DblList(strict=True)
        lst.push(value)
        assert lst.average() == avg

    @pytest.mark.lst_factory_data([i for i in range(1, 11)])
    def test_list_with_10_nodes_with_unque_values(self, strict_lst_factory):
        """10 nodes with values 1..10 should return an average of 5.5"""
        assert strict_lst_factory.average() == 5.5


class TestPeekMethods:
    def test_peek_with_empty_list(self):
        """Empty list returns None when you peek."""
        lst = DblList()
        assert not lst.peek()

    def test_peek_with_with_single_node(self, one_node):
        """List with single node should peek that node's value"""
        assert one_node.peek() == 1

    def test_peek_right_with_with_single_node(self, one_node):
        """List with single node should peek_right that node's value"""
        assert one_node.peek_right() == 1

    def test_peek_right_with_empty_list(self):
        """Empty list returns None when you peek."""
        lst = DblList()
        assert not lst.peek_right()

    def test_peek_right_with_with_2_nodes(self, one_node):
        """List with 2 nodes should peek_right that node's value"""
        assert one_node.peek_right() == 1


class TestFind:
    def test_find_with_empty_list(self):
        """Find on an empty list returns none."""
        lst = DblList()
        assert not lst.find(1)

    def test_find_value_single_node_match(self, one_node):
        """Find should return True if node matches in one node list."""
        assert one_node.find(1)

    def test_find_value_single_node_no_match(self, one_node):
        """Find should return False if node doesn't match in one node list."""
        assert not one_node.find(2)

    @pytest.mark.parametrize("value, result", [(i, True) for i in range(1, 10)])
    @pytest.mark.lst_factory_data([i for i in range(1, 11)])
    def test_list_10_nodes_with_unque_values(self, lst_factory, value, result):
        """List with 10 nodes, every node a match"""
        assert lst_factory.find(value) == result

    @pytest.mark.lst_factory_data([i for i in range(1, 11)])
    def test_list_10_nodes_no_matches(self, lst_factory):
        """List with 10 nodes, find value doesn't match"""
        assert not lst_factory.find(11)
