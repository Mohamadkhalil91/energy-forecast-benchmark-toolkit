import numpy as np
import pytest

from enfobench.evaluation.metrics import (
    mean_absolute_error,
    mean_bias_error,
    root_mean_squared_error,
    mean_squared_error,
    mean_absolute_percentage_error
)

all_metrics = [
    mean_absolute_error,
    mean_bias_error,
    root_mean_squared_error,
    mean_squared_error,
    mean_absolute_percentage_error,
]


@pytest.mark.parametrize("metric", all_metrics)
def test_metric_raises_with_nans(metric):
    with pytest.raises(ValueError):
        assert metric(np.array([1, 2, 3]), np.array([np.nan, 2, 3])) == 0

    with pytest.raises(ValueError):
        assert metric(np.array([1, np.nan, 3]), np.array([1, 2, 3])) == 0


@pytest.mark.parametrize("metric", all_metrics)
def test_metric_raises_with_unequal_length(metric):
    with pytest.raises(ValueError):
        assert metric(np.array([1, 2, 3]), np.array([])) == 0


@pytest.mark.parametrize("metric", all_metrics)
def test_metric_raises_with_empty_array(metric):
    with pytest.raises(ValueError):
        assert metric(np.array([1, 2, 3]), np.array([])) == 0

    with pytest.raises(ValueError):
        assert metric(np.array([]), np.array([1, 2, 3])) == 0


def test_mean_absolute_error():
    assert mean_absolute_error(np.array([1, 2, 3]), np.array([1, 2, 3])) == 0.
    assert mean_absolute_error(np.array([1, 2, 3]), np.array([2, 3, 4])) == 1.
    assert mean_absolute_error(np.array([1, 2, 3]), np.array([0, 1, 2])) == 1.


def test_mean_bias_error():
    assert mean_bias_error(np.array([1, 2, 3]), np.array([1, 2, 3])) == 0.
    assert mean_bias_error(np.array([1, 2, 3]), np.array([2, 3, 4])) == 1.
    assert mean_bias_error(np.array([1, 2, 3]), np.array([0, 1, 2])) == -1.
