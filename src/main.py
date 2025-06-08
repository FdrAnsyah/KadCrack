# src/main.py
import sys
import os
from src.cli import parse_args
from src.core.cracker import FileCracker

def main():
    args = parse_args()

    # Validasi argumen
    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

    if args.wordlist and (args.charset or args.min_length != 1 or args.max_length != 8):
        print("Error: Cannot combine dictionary attack with brute force options.")
        sys.exit(1)

    if not args.wordlist and not args.charset:
        print("Error: Please specify either a wordlist (-w) or brute force options (-m, -min, -max).")
        sys.exit(1)

    if args.wordlist and not os.path.exists(args.wordlist):
        print(f"Error: Wordlist file '{args.wordlist}' not found.")
        sys.exit(1)

    cracker = FileCracker(
        file_path=args.file,
        file_type=args.type,
        verbose=args.verbose,
        jobs=args.jobs
    )

    found_password = None
    if args.wordlist:
        found_password = cracker.run_dictionary_attack(args.wordlist)
    elif args.charset:
        found_password = cracker.run_brute_force_attack(
            args.charset, args.min_length, args.max_length
        )

    if found_password:
        print(f"\n[+] Password found: '{found_password}'")
        if args.output:
            try:
                with open(args.output, 'w') as f:
                    f.write(found_password)
                print(f"[+] Password saved to '{args.output}'")
            except Exception as e:
                print(f"Error saving password to file: {e}")
    else:
        print("\n[-] Password not found.")

if __name__ == "__main__":
    main()
