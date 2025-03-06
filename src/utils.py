"""Utility functions for the project."""

import numpy as np

def calculate_statistics(data):
    """Calculate basic statistics for the given data.

    Args:
        data (list or np.array): Numerical data

    Returns:
        dict: Dictionary containing mean, median, and std
    """
    data = np.array(data)
    return {
        "mean": np.mean(data),
        "median": np.median(data),
        "std": np.std(data)
    }

def normalize_data(data):
    """Normalize data to have zero mean and unit variance.

    Args:
        data (list or np.array): Data to normalize

    Returns:
        np.array: Normalized data
    """
    data = np.array(data)
    return (data - np.mean(data)) / np.std(data)