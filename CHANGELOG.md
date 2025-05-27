# 📄 CHANGELOG

All notable changes to **SaberSniff** will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/).

---

## [1.1.0] — 2025-05-27
### ✨ Added
- **Colorized terminal output** using `colorama`:
  - TCP → Light Green
  - UDP → Light Cyan
  - ICMP → Yellow
  - Unknown Protocols → Magenta
- **Hourly log rotation** system:
  - Log files saved in `logs/` folder
  - Filename format: `packets_YYYY-MM-DD_HH.log`
- **Timestamp printing** for:
  - Each captured packet
  - Program start
- **Protocol details in output**:
  - TCP/UDP ports
  - ICMP type and code
- **Graceful shutdown** on `Ctrl+C` (KeyboardInterrupt)
- Improved output formatting for readability

### 🔧 Changed
- Refactored the packet callback function for clarity and modularity
- Moved log file handling to a helper function

---

## [1.0.0] — 2025-05-25
### 🎉 Initial Release
- Basic IP packet sniffing with Scapy
- Output to terminal: Protocol, Source IP, Destination IP
- Simple logging to a flat file
