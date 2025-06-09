# KadCrack

**A Python-Based Password Cracker**

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## Table of Contents

* [About](#about)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)

  * [Basic Usage](#basic-usage)
  * [Dictionary Attack](#dictionary-attack)
  * [Brute Force Attack](#brute-force-attack)
  * [Advanced Options](#advanced-options)
* [Supported File Types](#supported-file-types)
* [Adding New File Types](#adding-new-file-types)
* [Contributing](#contributing)
* [License](#license)
* [Disclaimer](#disclaimer)

---

## About

**KadCrack** is a powerful and flexible Python tool designed to assist users in recovering lost or forgotten passwords from various types of encrypted files.
Unlike network-based brute-force tools, KadCrack focuses on **local file password cracking**, leveraging dictionary attacks and character-set based brute-force methods.

It aims to provide a **user-friendly command-line interface** with options for speed and efficiency.

> ⚠️ **Disclaimer:** This tool is intended for legitimate purposes only, such as recovering your own forgotten passwords or for security testing in environments where you have explicit permission. Unauthorized use against systems or files you do not own is illegal and unethical.

---

## Features

* 🗂️ **Dictionary Attack**: Crack passwords using a provided wordlist.
* 🧩 **Brute Force Attack**: Generate and test passwords based on specified character sets and length ranges.
* 🚀 **Multi-threading / Multi-processing**: Utilize multiple CPU cores for faster cracking.
* 📊 **Progress Tracking**: Real-time progress bar to monitor cracking status.
* 🛠️ **Modular Design**: Easy to extend and add support for new encrypted file formats.
* 💻 **Clear CLI**: User-friendly command-line interface with detailed help messages.

---

## Installation

To get KadCrack up and running on your system, follow these simple steps:

### 1. Clone the Repository

```bash
git clone https://github.com/FdrAnsyah/KadCrack.git
cd KadCrack
```

### 2. (Optional) Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
# venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

After activating your virtual environment (if you created one), you can start using **KadCrack** by running:

```bash
python -m src.main --help
```

### Basic Usage

```bash
python -m src.main [OPTIONS] <PATH_TO_ENCRYPTED_FILE>
```

You must specify the type of encrypted file using the `--type` argument.

#### Example:

```bash
python -m src.main --type zip --help
```

---

### Dictionary Attack

Attempts to crack the password using a predefined wordlist.
This is often the fastest method if you have a good wordlist.

#### Syntax:

```bash
python -m src.main <PATH_TO_FILE> --type <FILE_TYPE> -w <PATH_TO_WORDLIST>
```

#### Example:

```bash
python -m src.main ../Secret.zip --type zip -w /home/FileCrack/wordlists/rockyou.txt
```

Output:

```bash
[+] Starting Dictionary Attack on '../Secret.zip' (zip)...
Cracking: 377pass [00:02, 176.71pass/s]

[+] Password found: 'asikbanget'
```

---

### Brute Force Attack

Attempts to crack the password by systematically trying all possible combinations of characters.

#### Options:

* `-m`, `--charset`: Define the character set.

  * `lower` → lowercase letters (a-z)
  * `upper` → uppercase letters (A-Z)
  * `digits` → numbers (0-9)
  * `special` → common special characters (`!@#$%^&*()-_+=`)
  * **Combinations:** `lower,digits`, `lower,upper,digits,special`, etc.
* `-min`, `--min-length`: Minimum password length (default: 1)
* `-max`, `--max-length`: Maximum password length (default: 8)

#### Example 1:

```bash
python -m src.main my_document.pdf --type pdf -m lower -min 4 -max 6
```

#### Example 2:

```bash
python -m src.main important_report.docx --type doc -m lower,upper,digits -min 6 -max 8
```

---

### Advanced Options

* `-j`, `--jobs`: Number of concurrent processes/threads to use (default: 1).
* `-v`, `--verbose`: Enable verbose output.
* `-o`, `--output`: Save the found password to this file.

#### Example:

```bash
python -m src.main ../Secret.zip --type zip -w my_wordlist.txt -j 8
```

---

## Supported File Types

KadCrack currently supports (or is planned to support) the following file types:

* `.zip` → ZIP archives
* `.rar` → RAR archives
  *(Note: May require external tools like `unrar`)*
* `.pdf` → PDF documents
* `.doc`, `.xls`, `.ppt` → Microsoft Office documents

---

## Adding New File Types

KadCrack has a **modular architecture**, making it easy to extend:

1. Navigate to `src/` directory.
2. Create a new Python file (e.g., `src/new_file_type_handler.py`).
3. Implement the cracking logic with a function that takes:

   * file path
   * candidate password
     And returns `True` if the password is correct.
4. Integrate the new handler into `src/main.py` CLI logic.

---

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.

2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes.

4. Commit your changes:

   ```bash
   git commit -m 'Add new feature: brief description'
   ```

5. Push to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

6. Open a Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Disclaimer

This tool is provided **"as is,"** without warranty of any kind.
The authors are not responsible for any misuse or damage caused by this software.
Please use **responsibly and ethically**.

---

## Example Command Recap

```bash
python -m src.main ../Secret.zip --type zip -w /home/FileCrack/wordlists/rockyou.txt
```

```bash
[+] Starting Dictionary Attack on '../Secret.zip' (zip)...
Cracking: 377pass [00:02, 176.71pass/s]

[+] Password found: 'asikbanget'
```
