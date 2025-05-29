# SaberSniff

A simple, cross-platform Python packet sniffer for capturing and displaying raw network packets in real time.  
**SaberSniff** is designed for educational and diagnostic purposes, allowing you to inspect network traffic from your terminal with minimal setup.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Troubleshooting](#troubleshooting)
- [Legal Disclaimer](#legal-disclaimer)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Cross-platform:** Works on Windows, Linux, and macOS
- **No dependencies:** Pure Python, no external libraries required
- **Easy to use:** Run from Bash or CMD with a single command
- **Real-time packet display:** Shows source/destination IPs and protocols

---

## Requirements

- **Python 3.7+**
- **Administrator/root privileges** (required for raw socket access)

---

## Installation

1. **Clone this repository:**

    ```
    git clone https://github.com/UnknwnSaber/SaberSniff.git
    cd SaberSniff
    ```

2. **(Optional) Create a virtual environment:**

    ```
    python3 -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

3. **No dependencies to install!**  
   SaberSniff uses only the Python standard library.

---

## Usage

### Linux/macOS (Bash)

> **You must run as root to access raw sockets:**

