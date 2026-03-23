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
    """
    Read URLs from a CSV file.
    
    Args:
        filename: Path to the CSV file containing URLs
        
    Returns:
        List of URLs as strings
    """
    urls = []
    
    try:
        # Try different encodings to handle various CSV formats
        encodings = ['utf-8-sig', 'utf-8', 'latin-1', 'cp1252']
        
        file_opened = False
        for encoding in encodings:
            try:
                with open(filename, 'r', encoding=encoding, newline='') as file:
                    # Read the first line to check the header
                    first_line = file.readline().strip()
                    print(f"CSV Header detected: '{first_line}'")
                    
                    # Reset file pointer to beginning
                    file.seek(0)
                    
                    # Try reading as DictReader first
                    csv_reader = csv.DictReader(file)
                    
                    # Get the actual column names from the CSV
                    if csv_reader.fieldnames:
                        print(f"Column names found: {csv_reader.fieldnames}")
                        
                        # Find the column that contains URLs
                        url_column = None
                        for field in csv_reader.fieldnames:
                            field_clean = field.strip().lower()
                            if 'url' in field_clean:
                                url_column = field
                                break
                        
                        if url_column:
                            print(f"Using column: '{url_column}'")
                            
                            # Extract URLs from the identified column
                            for row in csv_reader:
                                url = row[url_column].strip()
                                if url and url.startswith('http'):
                                    urls.append(url)
                            
                            file_opened = True
                            break
                        else:
                            # If no 'urls' column, try reading as simple list
                            file.seek(0)
                            next(file)  # Skip header
                            for line in file:
                                url = line.strip()
                                if url and url.startswith('http'):
                                    urls.append(url)
                            file_opened = True
                            break
                    
            except (UnicodeDecodeError, UnicodeError):
                continue  # Try next encoding
            except Exception as e:
                print(f"Error with encoding {encoding}: {e}")
                continue
        
        if not file_opened:
            print(f"Error: Could not read file '{filename}' with any encoding.")
            return []
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        print(f"Current directory contents:")
        import os
        print(os.listdir('.'))
        return []
    except Exception as e:
        print(f"Unexpected error reading CSV file: {e}")
        return []
    
    return urls


def get_status_code(url: str) -> Tuple[int, str]:
    """
    Get the HTTP status code for a given URL.
    
    Args:
        url: The URL to check
        
    Returns:
        Tuple of (status_code, url)
    """
    try:
        # Set headers to mimic a real browser (some sites block scripts)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Send GET request with timeout and custom headers
        response = requests.get(url, timeout=10, headers=headers, allow_redirects=True)
        
        return (response.status_code, url)
        
    except requests.exceptions.Timeout:
        return (408, url)  # Request Timeout
        
    except requests.exceptions.ConnectionError:
        return (503, url)  # Service Unavailable
        
    except requests.exceptions.TooManyRedirects:
        return (310, url)  # Too Many Redirects
        
    except requests.exceptions.RequestException:
        return (500, url)  # Internal Server Error


def main():
    """
    Main function to read URLs from CSV and print their status codes.
    """
    # Define the input CSV filename (keeping original naming)
    csv_filename = 'Task 2 - Intern.csv'
    
    print(f"Reading URLs from '{csv_filename}'...\n")
    
    # Read all URLs from the CSV file
    urls = read_urls_from_csv(csv_filename)
    
    # Check if we got any URLs
    if not urls:
        print("\nNo URLs found to process.")
        print("\nTroubleshooting tips:")
        print("1. Make sure 'Task 2 - Intern.csv' is in the same folder as this script")
        print("2. Check that the CSV file has a header row with 'urls' column")
        print("3. Verify the CSV file is not corrupted")
        return
    
    print(f"\nFound {len(urls)} URLs. Starting status code checks...")
    print("This may take a few minutes...\n")
    print("=" * 100)
    
    # Process each URL and print result in required format
    for index, url in enumerate(urls, 1):
        # Get status code for this URL
        status_code, checked_url = get_status_code(url)
        
        # Print in required format: (STATUS CODE) URL
        print(f"({status_code}) {checked_url}")
        
        # Optional: Show progress every 20 URLs
        if index % 20 == 0:
            print(f"--- Processed {index}/{len(urls)} URLs ---")
    
    print("=" * 100)
    print(f"\n✓ Completed checking {len(urls)} URLs.")


if __name__ == "__main__":
    main()
