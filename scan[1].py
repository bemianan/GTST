#!/usr/bin/env python3

import sys
import nmap

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <ip> <class>")
    sys.exit(1)

ip = sys.argv[1]
ip_class = sys.argv[2].upper()

octets = ip.split('.')

if ip_class == "A":
    network = f"{octets[0]}.0.0.0/8"
elif ip_class == "B":
    network = f"{octets[0]}.{octets[1]}.0.0/16"
elif ip_class == "C":
    network = f"{octets[0]}.{octets[1]}.{octets[2]}.0/24"
else:
    print("Only classes A, B, and C are supported.")
    sys.exit(1)

print(f"Scanning network: {network}")

nm = nmap.PortScanner()
nm.scan(hosts=network, arguments="-sn")

print("\nLive hosts:")
for host in nm.all_hosts():
    print(f"{host} - {nm[host].state()}")
