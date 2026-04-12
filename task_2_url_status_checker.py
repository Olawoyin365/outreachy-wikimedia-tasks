#!/usr/bin/env python3
"""
Outreachy Task 2: URL Status Code Checker
Author: Ibrahim Jamiu
Description: Reads URLs from a CSV file and prints their HTTP status codes
"""

import csv
import requests
from typing import List, Tuple


def read_urls_from_csv(filename: str) -> List[str]:
    """Read URLs from a CSV file focusing on simplicity and robustness."""
    urls = []
    try:
        with open(filename, 'r', encoding='utf-8-sig', newline='') as file:
            csv_reader = csv.DictReader(file)
            # Find a column that looks like it contains URLs (handling typos like 'uls')
            url_col = None
            if csv_reader.fieldnames:
                for f in csv_reader.fieldnames:
                    f_low = f.lower().strip()
                    if 'url' in f_low or 'uls' in f_low or 'http' in f_low:
                        url_col = f
                        break
                # Fallback to the first column if no match is found
                if not url_col and csv_reader.fieldnames:
                    url_col = csv_reader.fieldnames[0]
            
            if url_col:
                for row in csv_reader:
                    url = row[url_col].strip()
                    if url.startswith('http'):
                        urls.append(url)
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    return urls


def get_status_code(url: str) -> Tuple[int, str]:
    """Get HTTP status code using a HEAD request for optimization."""
    try:
        # Use HEAD request as recommended by mentors to save bandwidth
        response = requests.head(url, timeout=10, allow_redirects=True)
        return (response.status_code, url)
    except requests.RequestException:
        # Fallback to GET if HEAD is not supported by the server
        try:
            response = requests.get(url, timeout=10, allow_redirects=True)
            return (response.status_code, url)
        except requests.RequestException:
            return (0, url)


def main():
    """Main function: concise implementation for URL status checking."""
    csv_filename = 'Task 2 - Intern.csv'
    urls = read_urls_from_csv(csv_filename)
    
    if not urls:
        print("No URLs found.")
        return

    # Process each URL and print result in required format: (STATUS CODE) URL
    for url in urls:
        status_code, checked_url = get_status_code(url)
        print(f"({status_code}) {checked_url}")


if __name__ == "__main__":
    main()
