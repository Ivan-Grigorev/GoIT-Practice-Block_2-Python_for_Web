import pytest


@pytest.fixture
def empty_dict():
    d = {"test": 1}
    return d


def test_update(empty_dict):
    empty_dict.update({"second": 2})
    assert len(empty_dict) == 2
    assert empty_dict["second"] == 2


def test_clear(empty_dict):
    empty_dict.clear()
    assert len(empty_dict) == 0
