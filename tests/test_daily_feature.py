import pytest

from src.daily_feature import process_items


def test_process_items_filters_and_squares():
    assert process_items([2, -1, 3]) == [4, 9]


def test_process_items_empty():
    assert process_items([]) == []
