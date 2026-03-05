import pandas as pd
import sys

def check_duplicates(file_path):
    """Check for duplicate words in a CSV file, case-insensitive."""
    try:
        df = pd.read_csv(file_path)
        if 'word' not in df.columns:
            print(f"Warning: 'word' column not found in {file_path}. Skipping.")
            return 0
        
        if df['word'].dtype != 'object':
            print(f"Warning: 'word' column in {file_path} is not of string type. Skipping duplicate check.")
            return 0

        # Check for empty words
        if df['word'].isnull().any() or df['word'].str.strip().eq('').any():
            print(f"Error: File {file_path} contains empty or whitespace-only words.")
            sys.exit(1)

        duplicates = df[df['word'].str.lower().duplicated(keep=False)]
        if not duplicates.empty:
            print(f"Error: Found duplicate words in {file_path}:")
            for word in duplicates['word'].unique():
                print(f"- {word}")
            sys.exit(1)
        
        print(f"Success: No duplicate words found in {file_path}.")
        return 0
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_duplicates.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    check_duplicates(file_path)
