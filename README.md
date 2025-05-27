# ⚔️ SaberSniff — Python Packet Sniffer

**SaberSniff** is a lightweight, terminal-based packet sniffer built with [Scapy](https://scapy.net/) and [Colorama](https://pypi.org/project/colorama/).  
It shows real-time, color-coded IP packet information and automatically rotates logs hourly. Designed for simplicity, readability, and quick analysis.

---

## 🚀 Features

- 📡 **Real-time IP Packet Capture**
- 🎨 **Colorized Output**:
  - **TCP** → Light Green
  - **UDP** → Light Cyan
  - **ICMP** → Yellow
  - **Unknown Protocols** → Magenta
- 🧾 **Detailed Packet Info**:
  - TCP/UDP ports
  - ICMP type and code
- 🕒 **Timestamps**:
  - Shown for every packet and at startup
- 🗃️ **Hourly Log Rotation**:
  - Logs saved in `logs/` folder
  - Filename format: `packets_YYYY-MM-DD_HH.log`
- 🛑 **Graceful Shutdown**:
  - Clean `Ctrl+C` exit with shutdown message
- 💻 **Terminal-Friendly**:
  - Minimal, readable, and easy to extend

---

## 📦 Requirements

- Python 3.6+
- [Scapy](https://scapy.net/)
- [Colorama](https://pypi.org/project/colorama/)
