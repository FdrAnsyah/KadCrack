# src/core/utils.py
import itertools
import string

def generate_charset(charset_name):
    """Generates a character set based on the given name."""
    if charset_name == 'lower':
        return string.ascii_lowercase
    elif charset_name == 'upper':
        return string.ascii_uppercase
    elif charset_name == 'digits':
        return string.digits
    elif charset_name == 'special':
        return string.punctuation
    elif charset_name == 'all':
        return string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    else:
        # Custom character set, e.g., 'abcdef123'
        return charset_name

def generate_bruteforce_passwords(charset, min_length, max_length):
    """Generates passwords for brute force attack."""
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(charset, repeat=length):
            yield "".join(combination)

def load_wordlist(wordlist_path):
    """Loads passwords from a wordlist file."""
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"Error: Wordlist file not found at {wordlist_path}")
        exit(1)
