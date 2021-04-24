import pytest
import random


@pytest.fixture
def mock_data():
    num_uids = {1426828011: 9,
                1426828028: 350,
                1426828037: 25,
                1426828056: 231,
                1426828058: 109,
                1426828066: 111,
                }
    return num_uids


@pytest.fixture
def data_gen():
    """
    Fixture for returning generator for creating a shuffled input with num same as uid
    """
    def factory(size):
        return iter(sorted(((x, x) for x in range(size)), key=lambda k: random.random()))
    return factory


@pytest.fixture
def find_keys():
    """
    Fixture returning factory for returning k largest keys from key_value dict
    using simple sort of all values
    """
    def factory(key_value, k):
        value_range = sorted(key_value.values(), reverse=True)[:k]
        return (key for key, value in key_value.items() if value in value_range)

    return factory


@pytest.fixture
def input_data():
    """
    Fixture returning factory for forming space sperated key, value string
    used as input as by main function
    """
    def factory(key_value):
        return (f"{key} {value}\n" for key, value in key_value.items())

    return factory
