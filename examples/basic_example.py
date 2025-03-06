"""Basic example demonstrating project functionality."""

import numpy as np
from src.utils import calculate_statistics, normalize_data

def main():
    # Generate sample data
    data = np.random.normal(loc=10, scale=2, size=1000)
    
    # Calculate statistics
    stats = calculate_statistics(data)
    print("\nData Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value:.2f}")
    
    # Normalize data
    normalized_data = normalize_data(data)
    normalized_stats = calculate_statistics(normalized_data)
    
    print("\nNormalized Data Statistics:")
    for key, value in normalized_stats.items():
        print(f"{key}: {value:.2f}")

if __name__ == "__main__":
    main()