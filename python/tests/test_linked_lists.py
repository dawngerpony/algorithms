""" Test linked lists. """
from data_structures.linked_lists import SinglyLinkedList


class TestSinglyLinkedList:
    """ Tests for singly linked list. """

    def test_initial_list(self):
        """ Singly linked list: test that a single node is created successfully. """
        lst = SinglyLinkedList()
        assert len(lst) == 1

    def test_insert_one(self):
        """ Test the insert method. """
        lst = SinglyLinkedList('apple')
        lst.insert('banana')
        assert len(lst) == 2

    def test_insert_two(self):
        """ Test the insert method. """
        lst = SinglyLinkedList('apple')
        assert len(lst) == 1
        lst.insert('banana')
        assert len(lst) == 2
        lst.insert('cherry')
        assert len(lst) == 3

    def test_search_success(self):
        """ Test a successful set of searches. """
        lst = SinglyLinkedList('apple')
        lst.insert('banana')
        lst.insert('cherry')
        lst.insert('damson')
        for fruit in ['apple', 'banana', 'cherry', 'damson']:
            node = lst.search(fruit)
            assert node.value() == fruit
        assert lst.search('pineapple') is None
