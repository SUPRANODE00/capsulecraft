#!/bin/bash
LOG_DIR="labs/witness_forensics/logs"
LOG_FILE="$LOG_DIR/alignment_stream.log"
mkdir -p "$LOG_DIR"

while true; do
    TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    # Termux compatible connection & network state check
    IFACE_STATE=$(ifconfig 2>/dev/null | awk '/wlan0|rmnet|ccmni/ {print "Interface:", $1}')
    SOCKET_COUNT=$(netstat -an 2>/dev/null | awk 'BEGIN {c=0} {c++} END {print "Total Connections:", c}')

    LOG_ENTRY="[$TIMESTAMP] TERMUX_ALIGNMENT | $IFACE_STATE | $SOCKET_COUNT"
    echo "$LOG_ENTRY" >> "$LOG_FILE"

    sleep 60
done
