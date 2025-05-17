import pytest

from linked_list import LinkedList, Node
from dbl_linked_list import DblList, DblNode

""" Linked List Fixtures. """


@pytest.fixture
def one_node():
    lst = LinkedList()
    lst.push(1)
    return lst


@pytest.fixture
def one_node_appended():
    lst = LinkedList()
    lst.append(1)
    return lst


@pytest.fixture
def lst_factory(request):
    marker = request.node.get_closest_marker("lst_factory_data")
    lst = LinkedList()
    for value in marker.args[0]:
        lst.push(value)
    return lst


@pytest.fixture
def strict_lst_factory(request):
    marker = request.node.get_closest_marker("lst_factory_data")
    lst = LinkedList(strict=True)
    for value in marker.args[0]:
        lst.push(value)
    return lst


@pytest.fixture
def lst_factory_append(request):
    marker = request.node.get_closest_marker("lst_factory_data")

    # Do something with the data
    lst = LinkedList()
    for value in marker.args[0]:
        lst.push(value)
    return lst


""" Dbl Linked List Fixtures. """


@pytest.fixture
def dbl_one_node():
    lst = DblList()
    lst.push(1)
    return lst


@pytest.fixture
def dbl_one_node_appended():
    lst = DblList()
    lst.append(1)
    return lst


@pytest.fixture
def dbl_lst_factory(request):
    marker = request.node.get_closest_marker("dbl_lst_factory_data")

    # Do something with the data
    lst = DblList()
    for value in marker.args[0]:
        lst.push(value)
    return lst


@pytest.fixture
def dbl_lst_factory_append(request):
    marker = request.node.get_closest_marker("dbl_lst_factory_data")

    # Do something with the data
    lst = DblList()
    for value in marker.args[0]:
        lst.push(value)
    return lst
