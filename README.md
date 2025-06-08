# FileCrack: A Python-Based Password Cracker

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
[![GitHub Issues](https://img.shields.io/github/issues/YOUR_GITHUB_USERNAME/FileCrack.svg)](https://github.com/YOUR_GITHUB_USERNAME/FileCrack/issues)
[![GitHub Stars](https://img.shields.io/github/stars/YOUR_GITHUB_USERNAME/FileCrack.svg)](https://github.com/YOUR_GITHUB_USERNAME/FileCrack/stargazers)

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

## About

FileCrack is a powerful and flexible Python tool designed to assist users in recovering lost or forgotten passwords from various types of encrypted files. Unlike network-based brute-force tools, FileCrack focuses on local file password cracking, leveraging dictionary attacks and character-set based brute-force methods. It aims to provide a user-friendly command-line interface with options for speed and efficiency.

**Disclaimer:** This tool is intended for legitimate purposes only, such as recovering your own forgotten passwords or for security testing in environments where you have explicit permission. Unauthorized use against systems or files you do not own is illegal and unethical.

## Features

* **Dictionary Attack:** Crack passwords using a provided wordlist.
* **Brute Force Attack:** Generate and test passwords based on specified character sets and length ranges.
* **Multi-threading/Multi-processing:** Utilize multiple CPU cores for faster cracking.
* **Progress Tracking:** Real-time progress bar to monitor cracking status.
* **Modular Design:** Easy to extend and add support for new encrypted file formats.
* **Clear CLI:** User-friendly command-line interface with detailed help messages.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/FileCrack.git](https://github.com/YOUR_GITHUB_USERNAME/FileCrack.git)
    cd FileCrack
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate # On Linux/macOS
    # venv\Scripts\activate # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To get started, activate your virtual environment (if you created one) and run `main.py`.

```bash
source venv/bin/activate # On Linux/macOS
# venv\Scripts\activate # On Windows

python src/main.py --help
