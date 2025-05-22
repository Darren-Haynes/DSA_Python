import pytest

from queue_ds import Queue, Node


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
        queue = Queue()
        assert hasattr(queue, "head")

    def test_Queue_initiates_with_head_as_None(self):
        """A Queue initializes with the .head attribute."""
        queue = Queue()
        assert not queue.head

    def test_Queue_initiates_with_tail_as_None(self):
        """A Queue initializes with the .tail attribute."""
        queue = Queue()
        assert not queue.tail

    def test_Queue_initiates_with_length_0(self):
        """A Queue initializes with the .length attribute."""
        queue = Queue()
        assert queue.length == 0


class TestEnqueueMethod:
    param_values = [(i, i) for i in range(1, 4)]

    def test_enqueue_one_node_correct_head_value(self):
        """If queue empty, head should become the value."""
        queue = Queue()
        queue.enqueue(1)
        assert queue.head.value == 1

    def test_enqueue_one_node_correct_tail_value(self):
        """If queue empty, tail should become the value."""
        queue = Queue()
        queue.enqueue(1)
        assert queue.tail.value == 1

    def test_enqueue_two_nodes_correct_tail_value(self):
        """When enqueue 2 nodes, the the last enqueued should be the tail"""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.tail.value == 2

    def test_enqueue_two_nodes_correct_tail_correct_prev_value(self):
        """When enqueue 2 nodes, the the first enqueued should be tail.prev value"""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.tail.prev.value == 1

    @pytest.mark.parametrize("num_of_nodes, queue_len", param_values)
    def test_enqueue_right_length(self, num_of_nodes, queue_len):
        """For each node added length should increase by one."""
        queue = Queue()
        for i in range(0, num_of_nodes):
            queue.enqueue(i)
        assert queue.length == queue_len


class TestDequeueMethod:
    def test_dequeue_empty_queue_returns_None(self):
        queue = Queue()
        assert not queue.dequeue()

    def test_queue_dequeue_one_node_head_is_none(self):
        """Dequeue queue with one node should have no head."""
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()
        assert not queue.head

    def test_queue_dequeue_one_node_tail_is_none(self):
        """Dequeue queue with one node should have no tail."""
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()
        assert not queue.tail

    def test_queue_dequeue_one_node_length_is_0(self):
        """Dequeue queue with one node should be length 0."""
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()
        assert queue.length == 0

    def test_queue_two_nodes_pop_one_correct_head(self):
        """Dequeue queue with two nodes has correct head."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        assert queue.head.value == 2

    def test_queue_two_nodes_pop_one_correct_tail(self):
        """Dequeue queue with two nodes has correct tail."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        assert queue.tail.value == 2

    def test_queue_two_nodes_pop_one_correct_length(self):
        """Dequeue queue with two nodes has correct length 1."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        assert queue.length == 1
