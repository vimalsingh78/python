"""Example demonstrating data analysis with pandas and matplotlib."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.utils import calculate_statistics

def generate_sample_data(size=1000):
    """Generate sample sales data."""
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', periods=size)
    
    data = {
        'date': dates,
        'sales': np.random.normal(1000, 200, size),
        'customers': np.random.randint(50, 200, size),
        'category': np.random.choice(['A', 'B', 'C'], size)
    }
    
    return pd.DataFrame(data)

def analyze_sales_data(df):
    """Analyze sales data and create visualizations."""
    # Calculate basic statistics
    sales_stats = calculate_statistics(df['sales'])
    print("\nSales Statistics:")
    for key, value in sales_stats.items():
        print(f"{key}: {value:.2f}")
    
    # Create visualizations
    plt.figure(figsize=(15, 10))
    
    # 1. Sales over time
    plt.subplot(2, 2, 1)
    plt.plot(df['date'], df['sales'])
    plt.title('Sales Over Time')
    plt.xticks(rotation=45)
    
    # 2. Sales distribution
    plt.subplot(2, 2, 2)
    plt.hist(df['sales'], bins=30)
    plt.title('Sales Distribution')
    
    # 3. Sales by category
    plt.subplot(2, 2, 3)
    df.boxplot(column='sales', by='category')
    plt.title('Sales by Category')
    
    # 4. Sales vs Customers scatter plot
    plt.subplot(2, 2, 4)
    plt.scatter(df['customers'], df['sales'])
    plt.xlabel('Number of Customers')
    plt.ylabel('Sales')
    plt.title('Sales vs Customers')
    
    plt.tight_layout()
    plt.show()
    
    # Additional analysis
    print("\nCategory-wise Analysis:")
    print(df.groupby('category')['sales'].agg(['mean', 'std', 'count']))

def main():
    # Generate and analyze data
    df = generate_sample_data()
    analyze_sales_data(df)
    
    # Demonstrate data manipulation
    print("\nTop 5 Sales Days:")
    top_sales = df.nlargest(5, 'sales')[['date', 'sales', 'customers']]
    print(top_sales)

if __name__ == "__main__":
    main()