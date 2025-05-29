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
    sudo python3 SaberSniff.py

### Windows (CMD)

> **Run Command Prompt as Administrator:**
    python SaberSniff.py
> 
---

## Example Output
[] SaberSniff Started
[] Listening for incoming packets...

Packet #1
Source IP: 192.168.1.5
Destination IP: 8.8.8.8
Protocol: 1

Packet #2
Source IP: 192.168.1.5
Destination IP: 192.168.1.1
Protocol: 6
...

---

## Troubleshooting

- **Permission denied / socket error:**  
  Run the script as root (Linux/macOS) or as Administrator (Windows).
- **Python not found:**  
  Ensure Python 3 is installed and added to your PATH.
- **No packets displayed:**  
  Make sure your firewall isn’t blocking raw sockets. Try running on a different network interface.

---

## Legal Disclaimer

> **Warning:**  
> SaberSniff is intended for educational and authorized network analysis only.  
> Intercepting network traffic without permission may violate laws or regulations.  
> Use responsibly and only on networks you own or have explicit authorization to analyze.

---

## Contributing

Contributions are welcome!  
Open an issue or submit a pull request to help improve SaberSniff.

---

## License

This project is licensed under the MIT License.  
See [LICENSE](LICENSE) for details.

---

**Happy Sniffing!**

*For questions or suggestions, feel free to open an issue on GitHub.*

