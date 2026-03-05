import pandas as pd
import sys
import os

def check_min_entries(file_path, min_entries):
    """Check if a CSV file meets the minimum number of entries."""
    try:
        df = pd.read_csv(file_path)
        num_entries = len(df)
        if num_entries < min_entries:
            print(f"Error: {file_path} has {num_entries} entries, which is less than the required minimum of {min_entries}.")
            sys.exit(1)
        
        print(f"Success: {file_path} meets the minimum entry requirement with {num_entries} entries.")
        return 0
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python check_min_entries.py <file_path> <min_entries>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        min_entries = int(sys.argv[2])
    except ValueError:
        print("Error: min_entries must be an integer.")
        sys.exit(1)
        
    check_min_entries(file_path, min_entries)
