from data_structures.bag import Bag


def test_bag_creation_is_empty():
    b = Bag()
    assert b.is_empty()


def test_bag_creation_is_not_empty():
    b = Bag()
    b.add(0)
    assert not b.is_empty()
