""" Test linked lists. """
from data_structures.linked_lists import SinglyLinkedList


class TestSinglyLinkedList:

    def test_initial_list(self):
        """ Singly linked list: test that a single node is created successfully. """
        lst = SinglyLinkedList()
        assert len(lst) == 1

    def test_insert(self):
        """ Test the insert method. """
        lst = SinglyLinkedList('apple')
        lst.insert('banana')
        assert len(lst) == 2

    def test_search_success(self):
        """ Test a successful set of searches. """
        lst = SinglyLinkedList('apple')
        lst.insert('banana')
        node = lst.search('apple')
        assert node.value() == 'apple'
        node = lst.search('banana')
        assert node.value() == 'banana'
