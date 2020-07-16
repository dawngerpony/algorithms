import pytest
from data_structures.stack import Stack


def test_stack_full():
    items = ["red", "blue", "green"]

    stack = Stack()

    for item in items:
        stack.push(item)

    assert stack.pop() == "green"
    assert stack.pop() == "blue"
    assert stack.pop() == "red"

    with pytest.raises(IndexError) as ie:
        stack.pop()
