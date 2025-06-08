# src/core/cracker.py
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
from src.core.utils import load_wordlist, generate_bruteforce_passwords, generate_charset
from src.core.formats.zip_cracker import ZipCracker
from src.core.formats.pdf_cracker import PdfCracker
import time

def crack_worker(args):
    """Worker function for multiprocessing."""
    file_path, file_type, password_attempt = args
    if file_type == "zip":
        cracker = ZipCracker(file_path)
    elif file_type == "pdf":
        cracker = PdfCracker(file_path)
    # Tambahkan else if untuk jenis file lainnya
    else:
        return None # Unsupported file type

    if cracker.try_password(password_attempt):
        return password_attempt
    return None

class FileCracker:
    def __init__(self, file_path, file_type, verbose=False, jobs=1):
        self.file_path = file_path
        self.file_type = file_type
        self.verbose = verbose
        self.jobs = min(jobs, cpu_count()) if jobs > 0 else 1 # Limit jobs to CPU count

    def run_dictionary_attack(self, wordlist_path):
        print(f"\n[+] Starting Dictionary Attack on '{self.file_path}' ({self.file_type})...")
        passwords = load_wordlist(wordlist_path)
        found_password = self._run_attack(passwords)
        return found_password

    def run_brute_force_attack(self, charset_name, min_length, max_length):
        print(f"\n[+] Starting Brute Force Attack on '{self.file_path}' ({self.file_type})...")
        charset = generate_charset(charset_name)
        if not charset:
            print("Error: Invalid character set provided.")
            return None

        # Estimate total combinations for progress bar
        total_combinations = sum(len(charset)**length for length in range(min_length, max_length + 1))
        print(f"[*] Estimated combinations: {total_combinations:,}")

        passwords = generate_bruteforce_passwords(charset, min_length, max_length)
        found_password = self._run_attack(passwords, total_combinations)
        return found_password

    def _run_attack(self, password_generator, total_combinations=None):
        found_password = None
        # Using Pool for multiprocessing
        with Pool(processes=self.jobs) as pool:
            # Prepare arguments for each worker
            # Passwords are iterated in the main process and chunked for workers
            args_iterator = ((self.file_path, self.file_type, p) for p in password_generator)

            # Use tqdm for a progress bar
            with tqdm(total=total_combinations, unit="pass", dynamic_ncols=True, desc="Cracking") as pbar:
                for result in pool.imap_unordered(crack_worker, args_iterator, chunksize=100):
                    if result:
                        found_password = result
                        pool.terminate() # Stop all workers once password is found
                        break
                    pbar.update(1) # Update progress for each tried password

        return found_password
