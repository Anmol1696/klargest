import pytest

from .. import models, utils


@pytest.mark.parametrize("k", range(6))
def test_k_largest(input_data, find_keys, mock_data, k):
    k_largest_keys = models.process_stream_to_get_keys(k, input_data(
        mock_data), extractor=utils.get_num_key_from_line)
    # Form expected output as list of str, since input is str
    expected_output = map(str, find_keys(mock_data, k))
    assert list(sorted(k_largest_keys)) == list(sorted(expected_output))


@pytest.mark.parametrize("k", range(6))
def test_k_largest_from_list_of_tuples_input(find_keys, mock_data, k):
    """
    Test case to pass input_iter as an list generator
    input iter is of form ((num, uid),..)
    """
    # Form data list of tuples from mock data dictionary
    data = ((value, key) for key, value in mock_data.items())
    k_largest_keys = models.process_stream_to_get_keys(k, data)
    assert list(sorted(k_largest_keys)) == list(
        sorted(find_keys(mock_data, k)))


def test_input_without_keys(size=10, k=3):
    """
    Test case where iterator is a list generator with tuple values
    """
    data = ((x,) for x in range(size))
    k_largest = models.KLargest.from_input_iter(k, data)
    assert list(sorted(k_largest.values)) == list(
        range(size-k, size))
    assert list(k_largest.keys) == []


def test_models_from_list_input(find_keys, mock_data, k=3):
    """
    Test case to pass input_iter as an list generator
    set extractor to return a tuple of single value
    """
    # Form data list of values from mock data dictionary
    data = [value for key, value in mock_data.items()]
    # Form expected output from data, taking the largest k values
    expeted = list(sorted(data, reverse=True))[:k]

    k_largest_obj = models.KLargest.from_input_iter(
        k, data, extractor=lambda x: (x,))
    assert list(sorted(k_largest_obj.values)) == expeted[::-1]


@pytest.mark.parametrize("k", [0.1, -1, "test", dict()])
def test_model_with_invalid_k_value(k):
    """
    Test case for invalid k values, must raise Exceptions
    """
    with pytest.raises(Exception):
        models.KLargest(k)


def test_k_gt_input_lenght(find_keys, mock_data):
    """
    Test case with k greater than length of input iter
    Expected output should return all the keys
    """
    k = len(mock_data) + 1
    k_largest_keys = models.process_stream_to_get_keys(
        k, ((value, key) for key, value in mock_data.items()))
    assert list(sorted(k_largest_keys)) == list(
        sorted(mock_data.keys()))


@pytest.mark.parametrize("size", [pow(10, x) for x in range(1, 6)])
def test_large_input(data_gen, size, k=5):
    data = data_gen(size)
    k_largest_keys = models.process_stream_to_get_keys(k, data)
    assert list(sorted(k_largest_keys)) == list(
        range(size-k, size))


def test_very_large_input_slowtest(size=10000000, k=10):
    """
    Slow test, takes about 30secs
    """
    data = ((x, x) for x in range(size))
    k_largest_keys = models.process_stream_to_get_keys(k, data)
    assert list(sorted(k_largest_keys)) == list(range(size-k, size))
