import sys
import os

def check_encoding(file_path):
    """Check if a file is UTF-8 encoded and has no BOM."""
    try:
        with open(file_path, 'rb') as f:
            bom = f.read(3)
            if bom == b'\xef\xbb\xbf':
                print(f"Error: File {file_path} is UTF-8 with BOM, which is not allowed.")
                sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while checking BOM: {e}")
        sys.exit(1)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.read()
        print(f"Success: File {file_path} is valid UTF-8 without BOM.")
        return 0
    except UnicodeDecodeError:
        print(f"Error: File {file_path} is not valid UTF-8.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_encoding.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    check_encoding(file_path)
