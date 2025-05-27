🕵️ SaberSniff - A Python Network Packet Sniffer by UnknwnSaber
SaberSniff is a powerful and lightweight network packet sniffer built using Python and Scapy. Designed for learning, diagnostics, and network analysis, it allows you to capture and inspect packets in real time with a clean, readable output.

⚙️ Dependencies
Python 3.x

Scapy (pip install scapy)

python
Copy code
from scapy.all import sniff  
from scapy.layers.inet import IP, TCP, UDP, ICMP  
🔍 Features
📡 Real-time packet sniffing on a specified network interface

🔎 Supports filtering by protocols: IP, TCP, UDP, ICMP

📁 Outputs detailed packet summaries for quick inspection

🧰 Easily customizable for deeper packet analysis or logging

🧼 Clean and minimal interface — ideal for scripting or terminal use

🚨 Disclaimer
SaberSniff is for educational and authorized use only.
Do not use this tool to capture traffic on networks you don’t own or have explicit permission to analyze.

🧠 Created by UnknwnSaber
Pull requests, suggestions, and forks are welcome. Expand it, break it, rebuild it.

Let me know if you'd like to include additional features like file logging, protocol stats, or GUI integration, and I can adjust the description accordingly.
