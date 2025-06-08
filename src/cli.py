# src/cli.py
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="FileCrack: A Python-based password cracker for various file types.",
        formatter_class=argparse.RawTextHelpFormatter # Untuk format help yang lebih baik
    )

    # Opsi Umum
    parser.add_argument(
        "file",
        help="Path to the encrypted file."
    )
    parser.add_argument(
        "-t", "--type",
        choices=["zip", "pdf", "rar", "doc", "xls", "ppt"], # Tambahkan jenis file lain yang didukung
        required=True,
        help="Type of the encrypted file (e.g., zip, pdf)."
    )
    parser.add_argument(
        "-o", "--output",
        help="Optional: Save the found password to this file."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output for more details during cracking."
    )

    # Opsi Dictionary Attack
    dict_group = parser.add_argument_group("Dictionary Attack Options")
    dict_group.add_argument(
        "-w", "--wordlist",
        help="Path to a wordlist file for dictionary attack."
    )

    # Opsi Brute Force Attack
    brute_group = parser.add_argument_group("Brute Force Attack Options")
    brute_group.add_argument(
        "-m", "--charset",
        help="Character set to use for brute force (e.g., 'lower' for lowercase, 'upper' for uppercase, 'digits', 'special', 'all')."
    )
    brute_group.add_argument(
        "-min", "--min-length",
        type=int,
        default=1,
        help="Minimum password length for brute force (default: 1)."
    )
    brute_group.add_argument(
        "-max", "--max-length",
        type=int,
        default=8,
        help="Maximum password length for brute force (default: 8)."
    )

    # Opsi Lanjutan
    advanced_group = parser.add_argument_group("Advanced Options")
    advanced_group.add_argument(
        "-j", "--jobs",
        type=int,
        default=1,
        help="Number of concurrent processes/threads to use for cracking (default: 1)."
    )

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    print("Parsed Arguments:")
    print(args)
