#!/bin/bash

# Check number of arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <IP_ADDRESS> <NSE_SCRIPT>"
    echo "Example: $0 192.168.1.1 vuln"
    exit 1
fi

TARGET=$1
SCRIPT=$2

echo "Scanning..."
nmap  --script "$SCRIPT" "$TARGET"
