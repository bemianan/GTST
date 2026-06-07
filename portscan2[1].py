#!/usr/bin/env python3

import nmap
nm = nmap.PortScanner()
target = input("Enter target IP address: ")
ports_to_scan = '22,80,8080'
nm.scan(hosts=target, ports=ports_to_scan)
for port in ports_to_scan.split(','):
    port = int(port)
    try:
        state = nm[target]['tcp'][port]['state']
        print(f"Port {port}: {state}")
    except KeyError:
        print(f"Port {port}: not scanned or no info")
