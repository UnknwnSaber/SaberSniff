from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from colorama import Fore, Style, init
import datetime
import os

# Initialize colorama
init(autoreset=True)

# Directory for logs
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_log_filename():
    # Rotate log file based on current hour
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H")
    return os.path.join(LOG_DIR, f"packets_{timestamp}.log")

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ip_layer.proto
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        # Initialize values
        protocol_name = "Unknown"
        color = Fore.MAGENTA  # Unknown
        extra = "No additional info"

        # Determine protocol and extract details
        if protocol == 1 and ICMP in packet:
            protocol_name = "ICMP"
            color = Fore.YELLOW
            extra = f"Type: {packet[ICMP].type}, Code: {packet[ICMP].code}"
        elif protocol == 6 and TCP in packet:
            protocol_name = "TCP"
            color = Fore.LIGHTGREEN_EX
            extra = f"Src Port: {packet[TCP].sport}, Dst Port: {packet[TCP].dport}"
        elif protocol == 17 and UDP in packet:
            protocol_name = "UDP"
            color = Fore.LIGHTCYAN_EX
            extra = f"Src Port: {packet[UDP].sport}, Dst Port: {packet[UDP].dport}"

        # Time of packet capture
        timestamp = datetime.datetime.now()

        # Print colorized output
        print(color + "=" * 70)
        print(color + f"Time       : {timestamp}")
        print(color + f"Protocol   : {protocol_name}")
        print(color + f"Source IP  : {src_ip}")
        print(color + f"Dest IP    : {dst_ip}")
        print(color + f"Details    : {extra}")
        print(color + "=" * 70 + "\n" + Style.RESET_ALL)

        # Log to time-rotated file
        log_line = f"{timestamp} | {protocol_name} | {src_ip} -> {dst_ip} | {extra}\n"
        with open(get_log_filename(), "a") as log_file:
            log_file.write(log_line)

def main():
    print(Fore.LIGHTBLUE_EX + f"[START] Packet Sniffer running at {datetime.datetime.now()}\n" + Style.RESET_ALL)
    try:
        sniff(prn=packet_callback, filter="ip", store=0)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[STOP] Packet sniffer interrupted by user (Ctrl+C)." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
# This script is a packet sniffer that captures and logs network packets.
# It uses Scapy to sniff packets and colorizes the output using Colorama.
