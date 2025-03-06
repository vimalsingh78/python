"""Example demonstrating web scraping with BeautifulSoup and requests."""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_python_jobs():
    """Scrape Python job listings from a jobs website."""
    # Using Python Jobs from realpython.com as an example
    url = "https://realpython.com/jobs/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        # Fetch the webpage
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find job listings (Note: selectors are examples)
        jobs = []
        for job in soup.select('.job-listing'):
            job_data = {
                'title': job.select_one('.job-title').text.strip(),
                'company': job.select_one('.company').text.strip(),
                'location': job.select_one('.location').text.strip(),
                'posted_date': job.select_one('.date').text.strip()
            }
            jobs.append(job_data)
        
        return pd.DataFrame(jobs)
    
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

def scrape_python_news():
    """Scrape Python-related news articles."""
    # Using Python.org news as an example
    url = "https://www.python.org/blogs/"
    
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find news articles
        articles = []
        for article in soup.select('.news-widget li'):
            article_data = {
                'title': article.select_one('a').text.strip(),
                'url': article.select_one('a')['href'],
                'date': article.select_one('.date').text.strip()
            }
            articles.append(article_data)
        
        return pd.DataFrame(articles)
    
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

def main():
    # Scrape job listings
    print("Scraping Python job listings...")
    jobs_df = scrape_python_jobs()
    if not jobs_df.empty:
        print("\nRecent Python Job Listings:")
        print(jobs_df.head())
        
        # Save to CSV
        jobs_df.to_csv('python_jobs.csv', index=False)
        print("\nJob listings saved to 'python_jobs.csv'")
    
    # Add delay to be respectful to servers
    time.sleep(2)
    
    # Scrape news articles
    print("\nScraping Python news articles...")
    news_df = scrape_python_news()
    if not news_df.empty:
        print("\nRecent Python News:")
        print(news_df.head())
        
        # Save to CSV
        news_df.to_csv('python_news.csv', index=False)
        print("\nNews articles saved to 'python_news.csv'")

if __name__ == "__main__":
    main()