""" Tests for the Bag class. """
from data_structures.bag import Bag


def test_bag_creation_is_empty():
    """ Test that a created bag is empty. """
    bag = Bag()
    assert bag.is_empty()


def test_bag_creation_is_not_empty():
    """ Test that a bag with one item in it is not empty. """
    bag = Bag()
    bag.add(0)
    assert not bag.is_empty()


def test_bag_len():
    """ Test the __len__ method of the bag. """
    bag = Bag()
    assert len(bag) == 0
    bag.add(0)
    assert len(bag) == 1


def test_bag_repr():
    """ Test the __repr__ method of the bag. """
    bag = Bag()
    assert repr(bag) == "Bag([])"
