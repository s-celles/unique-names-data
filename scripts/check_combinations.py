import pandas as pd
import sys
import os
import itertools
import requests

def download_profanity_list(url, local_path):
    """Download a profanity list from a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"Successfully downloaded profanity list to {local_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading profanity list: {e}")
        sys.exit(1)

def get_profanity_words(local_path):
    """Load profanity words from a local file."""
    with open(local_path, 'r', encoding='utf-8') as f:
        return {line.strip().lower() for line in f if line.strip()}

def check_combinations(dictionaries, blocklist_path, profanity_url):
    """Check for offensive combinations between dictionaries."""
    try:
        blocklist_df = pd.read_csv(blocklist_path)
        blocklist = set(blocklist_df['word'].str.lower())
    except FileNotFoundError:
        print(f"Warning: Blocklist not found at {blocklist_path}. Skipping blocklist check.")
        blocklist = set()
    except Exception as e:
        print(f"An error occurred while reading the blocklist: {e}")
        sys.exit(1)

    profanity_local_path = "profanity_list.txt"
    download_profanity_list(profanity_url, profanity_local_path)
    profanity_words = get_profanity_words(profanity_local_path)

    words_map = {}
    for name, path in dictionaries.items():
        try:
            df = pd.read_csv(path)
            words_map[name] = df['word'].str.lower().tolist()
        except FileNotFoundError:
            print(f"Error: Dictionary file not found at {path}")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred while reading {path}: {e}")
            sys.exit(1)

    problematic_combinations = []
    dict_names = list(words_map.keys())

    for i in range(len(dict_names)):
        for j in range(i + 1, len(dict_names)):
            dict1_name, dict2_name = dict_names[i], dict_names[j]
            dict1_words, dict2_words = words_map[dict1_name], words_map[dict2_name]
            
            # Check a sample of combinations
            sample_size = min(1000, len(dict1_words) * len(dict2_words))
            
            # This is a simplified sampling. For more robust testing, consider random sampling.
            combinations = list(itertools.product(dict1_words[:int(sample_size**0.5)], dict2_words[:int(sample_size**0.5)]))

            for word1, word2 in combinations:
                combo = f"{word1}{word2}".lower()
                if combo in blocklist or combo in profanity_words:
                    problematic_combinations.append(f"'{word1} {word2}' from [{dict1_name}, {dict2_name}]")

    if problematic_combinations:
        print("Error: Found problematic combinations:")
        for combo in problematic_combinations:
            print(f"- {combo}")
        sys.exit(1)

    print("Success: No problematic combinations found in the sample.")
    return 0

if __name__ == "__main__":
    # Example usage: python check_combinations.py adjectives:data/adjectives.csv colors:data/colors.csv animals:data/animals.csv
    if len(sys.argv) < 3:
        print("Usage: python check_combinations.py <dict1_name>:<dict1_path> <dict2_name>:<dict2_path> ...")
        sys.exit(1)
    
    dictionaries = {}
    for arg in sys.argv[1:]:
        try:
            name, path = arg.split(':', 1)
            dictionaries[name] = path
        except ValueError:
            print(f"Error: Invalid dictionary format '{arg}'. Expected 'name:path'.")
            sys.exit(1)

    blocklist_path = "data/blocklist.csv"
    profanity_url = "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"
    
    check_combinations(dictionaries, blocklist_path, profanity_url)
