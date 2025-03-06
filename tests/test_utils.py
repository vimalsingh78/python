"""Tests for utility functions."""

import numpy as np
import pytest
from src.utils import calculate_statistics, normalize_data

def test_calculate_statistics():
    """Test the calculate_statistics function."""
    data = [1, 2, 3, 4, 5]
    stats = calculate_statistics(data)
    
    assert isinstance(stats, dict)
    assert "mean" in stats
    assert "median" in stats
    assert "std" in stats
    assert np.isclose(stats["mean"], 3.0)
    assert np.isclose(stats["median"], 3.0)

def test_normalize_data():
    """Test the normalize_data function."""
    data = [1, 2, 3, 4, 5]
    normalized = normalize_data(data)
    
    assert len(normalized) == len(data)
    assert np.isclose(np.mean(normalized), 0)
    assert np.isclose(np.std(normalized), 1)